from typing import Optional
from semantix_genai_inference.inference.llm.alpaca import AlpacaInferenceClient
from semantix_genai_inference.inference.llm.llama2 import Llama2InferenceClient

class ModelClient:

    @staticmethod
    def create(client_type, inference_server_id: str, api_secret: Optional[str] = None, version: Optional[str] = "v0"):
        if client_type == "alpaca":
            return AlpacaInferenceClient(inference_server_id, api_secret, version=version)
        elif client_type == "llama2":
            return Llama2InferenceClient(inference_server_id, api_secret, version=version)
        else:
            raise Exception(f"Invalid model client type: {client_type}")