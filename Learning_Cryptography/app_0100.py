"""Application 100"""

# ********************
import os

os.system(command="cls")
# os.system(command="clear")
# ********************

print("." * 50)

# ********************
# ASCII:
# https://en.wikipedia.org/wiki/ASCII
# ASCII is American Standard Code for Information Interchange
print(2**7)  # = 128
# ********************
# Unicode:
# https://en.wikipedia.org/wiki/Unicode
# ********************
# UTF-8:
# https://en.wikipedia.org/wiki/UTF-8
# 1 to 4 Bytes
# Variable-length character encoding
# has maximal compatibility with ASCII
# ********************

print("." * 50)

# ********************
# We do not have 'nameof' similar C#
# pip install nameof
# https://github.com/alexmojaki/nameof
# ********************
key = "Ali"
print("key", type(key), len(key), key)
for item in key:
    print(item)

key = b"Ali"
print("key", type(key), len(key), key)
for item in key:
    print(item)

key = "Ali"
key_bytes = key.encode(encoding="utf-8")
print("key_bytes", type(key_bytes), len(key_bytes), key_bytes)
for item in key_bytes:
    print(item)

key = "Ali"
# Default Encoding: "utf-8"
key_bytes = key.encode()
print("key_bytes", type(key_bytes), len(key_bytes), key_bytes)
for item in key_bytes:
    print(item)
# ********************

print("." * 50)

# ********************
key = "علی"
print("key", type(key), len(key), key)
for item in key:
    print(item)

# دستور ذیل خطا می‌دهد
# non-ASCII character not allowed in bytes string literal
# Compile Error!
# key = b"علی"

key = "علی"
# دستور ذیل نیز خطا می‌دهد
# Runtime Error!
# key_bytes = key.encode(encoding="ascii")

# Default Encoding: "utf-8"
key_bytes = key.encode()
print("key_bytes", type(key_bytes), len(key_bytes), key_bytes)
for item in key_bytes:
    print(item)
# ********************

print("." * 50)

# ********************
# یک نکته کاربردی که زیاد سوال می‌شود
# ********************
message = "Hello\r\nWorld!"
print(message)

message_bytes = message.encode()
print(message_bytes)
# ********************

# ********************
# معادل دستور ذیل در سی‌شارپ
# System.Console.WriteLine(new string(c: '.',count: 50));
# با تشکر از مهندس داریوش اقتداری عزیز
print("." * 50)
# ********************

# ********************
# Decoding
# ********************
key = "Ali"
print("key", type(key), len(key), key)
key_bytes = key.encode()
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
key = key_bytes.decode()
print("key", type(key), len(key), key)
# ********************

print("." * 50)
