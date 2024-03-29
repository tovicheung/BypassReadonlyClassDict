# Modifying `sometype.__dict__`

`pip install bypassmappingproxy`

You can't directly set an attribute of a builtin type
```py
int.real = 69
```
`TypeError: cannot set 'real' attribute of immutable type 'int'`

You also can't modify `__dict__`
```py
int.__dict__["real"] = 69
```
`TypeError: 'mappingproxy' object does not support item assignment`

Mappingproxy provides a read-only proxy for mapping, which prevents modification. However, you can now bypass that using the `bypassmappingproxy` module

(it is written in **pure python**)


```py
import bypassmappingproxy as bmp

assert (1).real == 1
bmp.type_set(int, "real", 69)
assert (1).real == 69
```

[reference](https://github.com/python/cpython/issues/88004)
