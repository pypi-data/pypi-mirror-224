import torch,asyncio 
from typing import Any, Dict, Generator, List, Optional, Tuple
from threading import Thread
from transformers import TextIteratorStreamer, AutoTokenizer, AutoModelForCausalLM
from loguru import logger
from ..extras.misc import get_logits_processor, get_stopping_criteria
from ..extras.template import get_template 
from ..hparams import GeneratingArguments 

class ChatModel:
        
    def __init__(self) -> None:
        self.model, self.tokenizer,self.template,self.model_name = self.init_model()
        self.stop_ids = self.tokenizer.convert_tokens_to_ids(self.template.stop_words)
        self.generating_args = GeneratingArguments()

    def process_args(
        self,
        query: str,
        history: Optional[List[Tuple[str, str]]] = None,
        prefix: Optional[str] = None,
        **input_kwargs
    ) -> Tuple[Dict[str, Any], int]:

        prompt, _ = self.template.encode_oneturn(
            tokenizer=self.tokenizer, query=query, resp="", history=history, prefix=prefix
        )
        input_ids = torch.tensor([prompt], device=self.model.device)
        prompt_length = len(input_ids[0])

        do_sample = input_kwargs.pop("do_sample", None)
        temperature = input_kwargs.pop("temperature", None)
        top_p = input_kwargs.pop("top_p", None)
        top_k = input_kwargs.pop("top_k", None)
        repetition_penalty = input_kwargs.pop("repetition_penalty", None)
        max_length = input_kwargs.pop("max_length", None)
        max_new_tokens = input_kwargs.pop("max_new_tokens", None)

        gen_kwargs = self.generating_args.to_dict()
        gen_kwargs.update(dict(
            input_ids=input_ids,
            do_sample=do_sample if do_sample is not None else gen_kwargs["do_sample"],
            temperature=temperature or gen_kwargs["temperature"],
            top_p=top_p or gen_kwargs["top_p"],
            top_k=top_k or gen_kwargs["top_k"],
            repetition_penalty=repetition_penalty or gen_kwargs["repetition_penalty"],
            logits_processor=get_logits_processor(),
            stopping_criteria=get_stopping_criteria(self.stop_ids)
        ))

        if max_length:
            gen_kwargs.pop("max_new_tokens", None)
            gen_kwargs["max_length"] = max_length

        if max_new_tokens:
            gen_kwargs.pop("max_length", None)
            gen_kwargs["max_new_tokens"] = max_new_tokens

        return gen_kwargs, prompt_length
    
    def init_model(self):
        model_path = ""
        template = "default" 
        model_name = "default"
        logger.info(f"loading model: {model_path}...") 
    
        model = AutoModelForCausalLM.from_pretrained(
            model_path,
            trust_remote_code=True,
            low_cpu_mem_usage=True,
            torch_dtype=torch.float16,
            device_map='auto'
        )
        tokenizer = AutoTokenizer.from_pretrained(
            model_path,
            trust_remote_code=True,
            # llama不支持fast
            use_fast=False if model.config.model_type == 'llama' else True
        )
        
        model = model.eval().half().cuda()
    
        return model,tokenizer,get_template(template),model_name
    
    @torch.inference_mode() 
    def get_embedding(self,text: str,max_tokens):  
        if len(text)>max_tokens:
            text = text[:max_tokens]
        # 对长文本进行截断
        input_ids = self.tokenizer.encode(text, return_tensors='pt').to(self.model.device)
        with torch.no_grad():
            outputs = self.model.base_model(input_ids)
        embedding = outputs.last_hidden_state.float().cpu().squeeze(0).mean(0).numpy() 
        return embedding.tolist(),len(input_ids)
    
    @torch.inference_mode()
    def chat(
        self,
        query: str,
        history: Optional[List[Tuple[str, str]]] = None,
        prefix: Optional[str] = None,
        **input_kwargs
    ) -> Tuple[str, Tuple[int, int]]:
        gen_kwargs, prompt_length = self.process_args(query, history, prefix, **input_kwargs)
        generation_output = self.model.generate(**gen_kwargs)
        outputs = generation_output.tolist()[0][prompt_length:]
        response = self.tokenizer.decode(outputs, skip_special_tokens=True)
        response_length = len(outputs)
        return response, (prompt_length, response_length)

 
    @torch.inference_mode()
    async def stream_chat(
        self,
        query: str,
        history: Optional[List[Tuple[str, str]]] = None,
        prefix: Optional[str] = None,
        **input_kwargs
    ) -> Generator[str, None, None]:
        gen_kwargs, _ = self.process_args(query, history, prefix, **input_kwargs)
        streamer = TextIteratorStreamer(self.tokenizer, timeout=60.0, skip_prompt=True, skip_special_tokens=True)
        gen_kwargs["streamer"] = streamer

        thread = Thread(target=self.model.generate, kwargs=gen_kwargs)
        thread.start()
        
        for new_text in streamer:
            yield new_text
            await asyncio.sleep(0)  # 非阻塞休眠 
