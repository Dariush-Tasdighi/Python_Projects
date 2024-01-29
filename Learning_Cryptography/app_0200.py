# ********************
import os

os.system(command="cls")
# ********************

print("." * 50)

# ********************
key = "Ali"
print("key", type(key), len(key), key)

# دستور ذیل خطا می‌دهد
# می‌گیرد bytes چرا که ورودی
# key_hex = bytes.hex(key)

key_bytes = key.encode()
print("key_bytes", type(key_bytes), len(key_bytes), key_bytes)

key_hex = bytes.hex(key_bytes)
print("key_hex", type(key_hex), len(key_hex), key_hex)

key_bytes = bytes.fromhex(key_hex)
print("key_bytes", type(key_bytes), len(key_bytes), key_bytes)

key = key_bytes.decode()
print("key", type(key), len(key), key)
# ********************

print("." * 50)

# ********************
key = "علی"
print("key", type(key), len(key), key)

key_bytes = key.encode()
print("key_bytes", type(key_bytes), len(key_bytes), key_bytes)

key_hex = bytes.hex(key_bytes)
print("key_hex", type(key_hex), len(key_hex), key_hex)

key_bytes = bytes.fromhex(key_hex)
print("key_bytes", type(key_bytes), len(key_bytes), key_bytes)

key = key_bytes.decode()
print("key", type(key), len(key), key)
# ********************

print("." * 50)

# ********************
# simple_encrypt.py
# simple_decrypt.py
# ********************
