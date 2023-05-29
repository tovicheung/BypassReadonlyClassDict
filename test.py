import bypassmappingproxy as bmp

a = 1
print(a.real)
bmp.type_set(a, "real", 99)
print(a.real)