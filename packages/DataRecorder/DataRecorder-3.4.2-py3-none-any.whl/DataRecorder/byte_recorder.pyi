# -*- coding:utf-8 -*-
from pathlib import Path
from typing import Union, Optional

from .base import OriginalRecorder


class ByteRecorder(OriginalRecorder):
    SUPPORTS: tuple = ...
    __END: tuple = ...

    def __init__(self,
                 path: Optional[str, Path] = None,
                 cache_size: int = None): ...

    def add_data(self,
                 data: bytes,
                 seek: int = None) -> None: ...

    def _record(self) -> None: ...
