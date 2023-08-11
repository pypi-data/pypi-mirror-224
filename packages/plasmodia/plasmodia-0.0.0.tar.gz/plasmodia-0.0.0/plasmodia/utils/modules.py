import sys
from types import ModuleType
from typing import Protocol, runtime_checkable

ModuleId = ModuleType | str


@runtime_checkable
class Factory(Protocol):
    def get(self, name: str) -> type:
        ...


def _get_module(module: ModuleId) -> ModuleType:
    if isinstance(module, str):
        try:
            module = sys.modules[module]
        except KeyError:
            raise ValueError(f"The given module {module} is not valid.")

    return module


def _get_submodule(module: ModuleId, name: str) -> ModuleType | None:
    module = _get_module(module)
    return getattr(module, name, None)


def factory(module: ModuleId) -> Factory | None:
    retrieved = _get_submodule(module, "factories")

    if not isinstance(retrieved, Factory):
        return None

    return retrieved


def interface(module: ModuleId) -> ModuleType | None:
    return _get_submodule(module, "interfaces")


def verify(module: ModuleId):
    if factory(module) is None:
        raise FileNotFoundError(f"Factory for {module} is missing.")

    if interface(module) is None:
        raise FileNotFoundError(f"Interface for {module} is missing.")
