import os
from pydantic import BaseModel, parse_obj_as
from typing import List, Optional
import httpx

with open(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "VERSION"), "r"
) as f:
    __version__ = f.read().strip()

api_key = None
base_url = None


class Choice(BaseModel):
    text: str
    index: int
    finish_reason: str


class CompletionResponse(BaseModel):
    id: str
    object: str
    created: int
    model: str
    choices: List[Choice]


class Model(BaseModel):
    id: str
    object: str
    created: int


class ListModelsResponse(BaseModel):
    object: str
    data: List[Model]


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatCompletionResponseChoice(BaseModel):
    index: int
    message: ChatMessage
    finish_reason: Optional[str]


class UsageInfo(BaseModel):
    prompt_tokens: int
    total_tokens: int
    completion_tokens: Optional[int]


class ChatCompletionResponse(BaseModel):
    id: str
    object: str
    created: int
    model: str
    choices: List[ChatCompletionResponseChoice]
    usage: UsageInfo


class FireworksClient:
    def __init__(self, request_timeout=600, **kwargs):
        if "request_timeout" in kwargs:
            request_timeout = kwargs["request_timeout"]
        self.api_key = api_key or os.environ.get("FIREWORKS_API_KEY")
        if not self.api_key:
            raise ValueError(
                "No API key provided. You can set your API key in code using 'fireworks.client.api_key = <API-KEY>', or you can set the environment variable FIREWORKS_API_KEY=<API-KEY>)."
            )
        self.base_url = base_url or os.environ.get(
            "FIREWORKS_BASE_URL", "https://api.fireworks.ai/inference/v1"
        )
        self.client = httpx.Client(
            headers={"Authorization": f"Bearer {self.api_key}"},
            timeout=request_timeout,
            **kwargs,
        )

    def _get_request(self, url):
        resp = self.client.get(url)
        resp.raise_for_status()
        return resp.json()

    def _post_request(self, url, data=None):
        resp = self.client.post(url, json=data)
        resp.raise_for_status()
        return resp.json()

    async def _post_request_async(self, url, data=None):
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                url, headers={"Authorization": f"Bearer {self.api_key}"}, json=data
            )
        resp.raise_for_status()
        return resp.json()


class Completion:
    @classmethod
    def create(cls, model, prompt, request_timeout=600, **kwargs):
        client = FireworksClient(request_timeout=request_timeout)
        data = {"model": model, "prompt": prompt, **kwargs}
        response = client._post_request(f"{client.base_url}/completions", data=data)
        return parse_obj_as(CompletionResponse, response)

    @classmethod
    async def acreate(cls, model, prompt, request_timeout=600, **kwargs):
        client = FireworksClient(request_timeout=request_timeout)
        data = {"model": model, "prompt": prompt, **kwargs}
        response = await client._post_request_async(
            f"{client.base_url}/completions", data=data
        )
        return parse_obj_as(CompletionResponse, response)


class ChatCompletion:
    @classmethod
    def create(cls, model, messages, request_timeout=600, **kwargs):
        client = FireworksClient(request_timeout=request_timeout)
        data = {"model": model, "messages": messages, **kwargs}
        response = client._post_request(
            f"{client.base_url}/chat/completions", data=data
        )
        return parse_obj_as(ChatCompletionResponse, response)

    @classmethod
    async def acreate(cls, model, messages, request_timeout=600, **kwargs):
        client = FireworksClient(request_timeout=request_timeout)
        data = {"model": model, "messages": messages, **kwargs}
        response = await client._post_request_async(
            f"{client.base_url}/chat/completions", data=data
        )
        return parse_obj_as(ChatCompletionResponse, response)


@classmethod
def _list_models(cls, request_timeout=60):
    client = FireworksClient(request_timeout=request_timeout)
    response = client._get_request(f"{client.base_url}/models")
    return parse_obj_as(ListModelsResponse, response)


Model.list = _list_models
