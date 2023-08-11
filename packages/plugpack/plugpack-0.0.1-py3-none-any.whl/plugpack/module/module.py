# -*- coding: utf-8 -*-

from types import ModuleType
from typing import Union

from plugpack.module.mixin.module_async_open import ModuleAsyncOpen
from plugpack.module.mixin.module_doc import ModuleDoc
from plugpack.module.mixin.module_logger import ModuleLogger
from plugpack.module.mixin.module_open import ModuleOpen
from plugpack.module.mixin.module_version import ModuleVersion


class Module(
    ModuleAsyncOpen,
    ModuleDoc,
    ModuleLogger,
    ModuleOpen,
    ModuleVersion,
):
    def __init__(self, module: Union[str, ModuleType], isolate=False, *args, **kwargs):
        if isinstance(module, str):
            self._module = self.import_module(module, isolate=isolate)
        else:
            self._module = module
        self._args = args
        self._kwargs = kwargs

    def open(self) -> None:
        if not self.has_on_open:
            return
        self.on_open(*self._args, **self._kwargs)

    def close(self) -> None:
        if not self.has_on_close:
            return
        self.on_close()

    async def async_open(self) -> None:
        if not self.has_on_async_open:
            return
        await self.on_async_open(*self._args, **self._kwargs)

    async def async_close(self) -> None:
        if not self.has_on_async_close:
            return
        await self.on_async_close()
