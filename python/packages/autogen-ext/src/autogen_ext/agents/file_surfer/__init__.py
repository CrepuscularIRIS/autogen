try:
    from ._file_surfer import FileSurfer
except ImportError as e:
    raise ImportError(
        "Dependencies for the file surfer agent not found. "
        "Please install the required extras: "
        "pip install autogen-ext[file-surfer]"
    ) from e

__all__ = ["FileSurfer"]
