"""
"""

import sys

from .config import Config
from .gpu.decorator import GPU
from .gpu.torch import disable_cuda_intercept
from .gradio import gradio_auto_wrap
from .gradio import disable_gradio_auto_wrap
from .gradio import enable_gradio_auto_wrap


if Config.zero_gpu and sys.version_info.minor < 9: # pragma: no cover
    raise RuntimeError("Actually using @spaces.GPU on a ZeroGPU Space requires Python 3.9+")


__all__ = [
    'GPU',
    'disable_cuda_intercept',
    'gradio_auto_wrap',
    'disable_gradio_auto_wrap',
    'enable_gradio_auto_wrap',
]
