try:
    from ._multimodal_web_surfer import MultimodalWebSurfer
    from .playwright_controller import PlaywrightController
except ImportError as e:
    raise ImportError(
        "Dependencies for the web surfer agent not found. "
        "Please install the required extras: "
        "pip install autogen-ext[web-surfer]"
    ) from e

__all__ = ["MultimodalWebSurfer", "PlaywrightController"]
