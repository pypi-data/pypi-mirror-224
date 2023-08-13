import time,shortuuid
from enum import Enum
from pydantic import BaseModel, Field 
from typing import ( 
    Any,
    Callable, 
    List, 
    Optional, 
    Union,
    Dict 
)

class Role(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"


class Finish(str, Enum):
    STOP = "stop"
    LENGTH = "length" 
    
class ModelCard(BaseModel):
    id: str
    object: Optional[str] = "model"
    created: Optional[int] = Field(default_factory=lambda: int(time.time()))
    owned_by: Optional[str] = "owner"
    root: Optional[str] = None
    parent: Optional[str] = None
    permission: Optional[list] = []


class ModelList(BaseModel):
    object: Optional[str] = "list"
    data: Optional[List[ModelCard]] = [] 
 
class ChatMessage(BaseModel):
    role: Role
    content: str


class DeltaMessage(BaseModel):
    role: Optional[Role] = None
    content: Optional[str] = None


class ChatCompletionRequest(BaseModel):
    model: str
    messages: List[ChatMessage]
    temperature: Optional[float] = None
    top_p: Optional[float] = None
    n: Optional[int] = 1
    max_tokens: Optional[int] = None
    stream: Optional[bool] = False


class ChatCompletionResponseChoice(BaseModel):
    index: int
    message: ChatMessage
    finish_reason: Finish


class ChatCompletionResponseStreamChoice(BaseModel):
    index: int
    delta: DeltaMessage
    finish_reason: Optional[Finish] = None


class ChatCompletionResponseUsage(BaseModel):
    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0

class EmbeddingsRequest(BaseModel): 
    input: Union[List[str],str] = ["string"]
    model: Optional[str] = None
    encoding_format: Optional[str] = "base64"
    max_tokens: Optional[int] = 1024
 
class EmbeddingsResponse(BaseModel):
    object: str = "list"
    data: List[Dict[str, Any]]
    model: str
    usage: ChatCompletionResponseUsage

class ChatCompletionResponse(BaseModel):
    id: str = Field(default_factory=lambda: f"chatcmpl-{shortuuid.random()}")
    object: Optional[str] = "chat.completion"
    created: Optional[int] = Field(default_factory=lambda: int(time.time()))
    model: str
    choices: List[ChatCompletionResponseChoice]
    usage: ChatCompletionResponseUsage


class ChatCompletionStreamResponse(BaseModel):
    id: str = Field(default_factory=lambda: f"chatcmpl-{shortuuid.random()}")
    object: Optional[str] = "chat.completion.chunk"
    created: Optional[int] = Field(default_factory=lambda: int(time.time()))
    model: str
    choices: List[ChatCompletionResponseStreamChoice] 
    
    def to_dict(self):
        return {'data': self.__dict__}
    def json(
        self,
        *,
        include: Optional[Union['AbstractSetIntStr', 'MappingIntStrAny']] = None,
        exclude: Optional[Union['AbstractSetIntStr', 'MappingIntStrAny']] = None,
        by_alias: bool = False,
        skip_defaults: Optional[bool] = None,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
        exclude_none: bool = False,
        encoder: Optional[Callable[[Any], Any]] = None,
        models_as_dict: bool = True,
        **dumps_kwargs: Any,
    ) -> str:
        response = super().json(include = include,
                             exclude = exclude,
                             by_alias = by_alias,
                             skip_defaults = skip_defaults,
                             exclude_unset = exclude_unset,
                             exclude_defaults = exclude_defaults,  
                             exclude_none = exclude_none,
                             encoder = encoder, 
                             models_as_dict = models_as_dict,
                             **dumps_kwargs)
        response = "data: " + response + "\n\n"
        return response
