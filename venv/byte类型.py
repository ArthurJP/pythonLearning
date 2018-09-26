print("ABC".encode("GBK"))

print("中文".encode("utf-8"))



print(b"ssy".decode("GBK"))

print(b"\xe4\xb8\xad\xe6\x96\x87".decode("utf-8"))

print(b"\xe4\xb8\xad\xff".decode("utf-8","replace"))