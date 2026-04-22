try:
    from ._ollama_client import OllamaChatCompletionClient
    from .config import (
        BaseOllamaClientConfigurationConfigModel,
        CreateArgumentsConfigModel,
    )
except ImportError as e:
    raise ImportError(
        "Dependencies for the Ollama client not found. "
        "Please install the required extras: "
        "pip install autogen-ext[ollama]"
    ) from e

__all__ = [
    "OllamaChatCompletionClient",
    "BaseOllamaClientConfigurationConfigModel",
    "CreateArgumentsConfigModel",
]
