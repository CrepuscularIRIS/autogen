try:
    from . import _message_transform
    from ._openai_client import (
        AZURE_OPENAI_USER_AGENT,
        AzureOpenAIChatCompletionClient,
        BaseOpenAIChatCompletionClient,
        OpenAIChatCompletionClient,
    )
    from .config import (
        AzureOpenAIClientConfigurationConfigModel,
        BaseOpenAIClientConfigurationConfigModel,
        CreateArgumentsConfigModel,
        OpenAIClientConfigurationConfigModel,
    )
except ImportError as e:
    raise ImportError(
        "Dependencies for the OpenAI client not found. "
        "Please install the required extras: "
        "pip install autogen-ext[openai]"
    ) from e

__all__ = [
    "OpenAIChatCompletionClient",
    "AzureOpenAIChatCompletionClient",
    "BaseOpenAIChatCompletionClient",
    "AzureOpenAIClientConfigurationConfigModel",
    "OpenAIClientConfigurationConfigModel",
    "BaseOpenAIClientConfigurationConfigModel",
    "CreateArgumentsConfigModel",
    "AZURE_OPENAI_USER_AGENT",
    "_message_transform",
]
