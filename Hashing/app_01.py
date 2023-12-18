"""Learning Hashing (String)"""

# ********************
# print('Hello, World!')
print("Hello, World!")
print("Hello, World!")
print("Hello, World!")
print("Hello, World!")
print("Hello, World!")
# ********************

# ********************
# import os

# # os.system("cls")
# os.system(command="cls")

# print("Hello, World!")
# print("Hello, World!")
# print("Hello, World!")
# print("Hello, World!")
# print("Hello, World!")
# ********************

# ********************
# Alias Name
# ********************
# import os as googooli

# googooli.system(command="cls")

# print("Hello, World!")
# print("Hello, World!")
# print("Hello, World!")
# print("Hello, World!")
# print("Hello, World!")
# ********************

# ********************
# # import os, hashlib

# import os
# import hashlib

# os.system(command="cls")

# # PASSWORD = "MyPassword"

# password = input("What is your password: ")
# print(password)

# # encoded_password = password.encode(encoding="utf-8")
# # encodedPassword = password.encode(encoding="utf-8")
# encoded_password = password.encode()
# print(encoded_password)

# md5_hashed_password_object = hashlib.md5(encoded_password)
# print(type(md5_hashed_password_object), md5_hashed_password_object)

# MD5_HASHED_PASSWORD = md5_hashed_password_object.hexdigest()
# print(type(MD5_HASHED_PASSWORD), MD5_HASHED_PASSWORD, len(MD5_HASHED_PASSWORD))
# ********************

# ********************
# import os
# import hashlib

# os.system(command="cls")

# password = input("What is your password: ")
# print(password)

# encoded_password = password.encode(encoding="utf-8")

# md5_hashed_password_object = hashlib.md5(encoded_password)
# MD5_HASHED_PASSWORD = md5_hashed_password_object.hexdigest()
# print(MD5_HASHED_PASSWORD, len(MD5_HASHED_PASSWORD))

# sha1_hashed_password_object = hashlib.sha1(encoded_password)
# SHA1_HASHED_PASSWORD = sha1_hashed_password_object.hexdigest()
# print(SHA1_HASHED_PASSWORD, len(SHA1_HASHED_PASSWORD))

# sha256_hashed_password_object = hashlib.sha256(encoded_password)
# SHA256_HASHED_PASSWORD = sha256_hashed_password_object.hexdigest()
# print(SHA256_HASHED_PASSWORD, len(SHA256_HASHED_PASSWORD))

# sha512_hashed_password_object = hashlib.sha512(encoded_password)
# SHA512_HASHED_PASSWORD = sha512_hashed_password_object.hexdigest()
# print(SHA512_HASHED_PASSWORD, len(SHA512_HASHED_PASSWORD))
# ********************

# ********************
# Base 64: 0..9 and A..F = 16
# ********************

# ********************
# #                            32
# # MD5: 32: 16 * ... * 16 = 16
# print(16**32)
# # 340282366920938463463374607431768211456
# #                             40
# # SHA1: 40: 16 * ... * 16 = 16
# print(16**40)
# # 1461501637330902918203684832716283019655932542976
# #                               64
# # SHA256: 64: 16 * ... * 16 = 16
# print(16**64)
# # 115792089237316195423570985008687907853269984665640564039457584007913129639936
# ********************

# ********************
# pip install pycryptodome
# https://www.pycryptodome.org/
# https://github.com/Legrandin/pycryptodome/
# ********************
# import os
# from Crypto.Hash import MD4

# os.system(command="cls")

# password = input("What is your password: ")
# print(password)

# encoded_password = password.encode(encoding="utf-8")

# md4_hashed_password_object = MD4.new(data=encoded_password)
# MD4_HASHED_PASSWORD = md4_hashed_password_object.hexdigest()
# print(MD4_HASHED_PASSWORD, len(MD4_HASHED_PASSWORD))
# ********************
