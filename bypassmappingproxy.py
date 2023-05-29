from typing import Any
from types import MappingProxyType as mappingproxy

import gc

def proxy_get_dict(proxy: mappingproxy) -> dict:
    """returns the underlying dictionary of the mappingproxy"""
    refs = gc.get_referents(proxy)
    return refs[0]

def proxy_set(proxy: mappingproxy, key: str, value: Any):
    """set value of mappingproxy (which you shouldn't be able to)"""
    proxy_get_dict(proxy)[key] = value

def type_set(typ: type, name: str, value: Any):
    proxy_set(typ.__dict__, name, value)