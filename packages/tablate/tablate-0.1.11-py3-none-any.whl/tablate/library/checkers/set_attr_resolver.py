from typing import Any


def set_attr_resolver(instance: Any, attr: str, default: Any):
    return instance.__getattribute__(attr) if hasattr(instance, attr) and instance.__getattribute__(attr) is not None else default

