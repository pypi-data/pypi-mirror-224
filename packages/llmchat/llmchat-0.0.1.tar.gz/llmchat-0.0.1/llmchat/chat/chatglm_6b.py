import torch,asyncio
from typing import Generator, List, Optional, Tuple 
from transformers import AutoModel, AutoTokenizer 
from .stream_chat import ChatModel as ChatBaseModel 
from ..extras.template import get_template   

class ChatModel(ChatBaseModel): 
    
    def init_model(self):
        model_path = r"E:/opt/huggingface/hub/silver--chatglm-6b-int4-slim" 
        template = "chatglm"
        model_name = "chatglm-6b"
        tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
        model = AutoModel.from_pretrained( model_path, trust_remote_code=True).half().cuda()
        model.eval()
        return model,tokenizer,get_template(template),model_name
    
    @torch.inference_mode()
    def get_embedding(self,text: str,max_tokens):  
        if len(text)>max_tokens:
            text = text[:max_tokens]
        # 对长文本进行截断
        input_ids = self.tokenizer.encode(text, return_tensors='pt').to(self.model.device)
        with torch.no_grad():
            outputs = self.model.base_model(input_ids)
        embedding = outputs.last_hidden_state.float().cpu().squeeze(0).mean(0).numpy()[0] 
        return embedding.tolist(),len(input_ids)

    @torch.inference_mode()
    def chat(
        self, query: str, history: Optional[List[Tuple[str, str]]] = None, prefix: Optional[str] = None, **input_kwargs
    ) -> Tuple[str, Tuple[int, int]]:
          
        if history is None:
            history = []  
         
        gen_kwargs, prompt_length = self.process_args(query, history, prefix, **input_kwargs)
        try:
            del gen_kwargs["input_ids"] 
        except:
            pass
        try:
            del gen_kwargs["max_new_tokens"] 
        except:
            pass
        
        response, _ = self.model.chat(self.tokenizer, query, history,**gen_kwargs)
     
        response_length = len(response)
        return response, (prompt_length, response_length)
    
    @torch.inference_mode()
    async def stream_chat(
        self, query: str, history: Optional[List[Tuple[str, str]]] = None, prefix: Optional[str] = None, **input_kwargs
    ) -> Generator[str, None, None]:
    
        if history is None:
            history = []  
    
        gen_kwargs, _ = self.process_args(query, history, prefix, **input_kwargs)
        try:
            del gen_kwargs["input_ids"] 
        except:
            pass
        try:
            del gen_kwargs["max_new_tokens"] 
        except:
            pass
    
        sends = 0 
        for response, _ in self.model.stream_chat(self.tokenizer, query, history, **gen_kwargs): 
            next_text = response[sends:]
            # https://github.com/THUDM/ChatGLM-6B/issues/478
            # 修复表情符号的输出问题
            if "\uFFFD" == next_text[-1:]:
                continue
            sends = len(response) 
    
            yield next_text
            await asyncio.sleep(0)  # 非阻塞休眠 
    
 