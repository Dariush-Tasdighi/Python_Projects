# ********************
# pip install cryptography
# ********************
# https://github.com/pyca/cryptography
# https://pypi.org/project/cryptography
# ********************
# https://cryptography.io/en/latest
# https://cryptography.io/en/latest/fernet/
# https://github.com/fernet/spec/blob/master/Spec.md
# ********************
# https://en.wikipedia.org/wiki/Advanced_Encryption_Standard
# ********************
# https://elc.github.io/python-security/chapters/06_Symmetric_Encryption.html
# https://elc.github.io/python-security/chapters/07_Asymmetric_Encryption.html
# ********************

# ********************
import os

os.system(command="cls")
# ********************

print("." * 50)

# ********************
from cryptography.fernet import Fernet

key = Fernet.generate_key()
print("key", type(key), len(key), key)
# ********************

print("." * 50)

# ********************
from cryptography.fernet import Fernet

for _ in range(5):
    key = Fernet.generate_key()
    print("key", type(key), len(key), key)
# ********************

print("." * 50)
