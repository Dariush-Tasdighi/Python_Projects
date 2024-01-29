# ********************
import os

os.system(command="cls")
# ********************

print("." * 50)

# ********************
from cryptography.fernet import Fernet

key = Fernet.generate_key()
print("key", type(key), len(key), key)

fernet_object = Fernet(key=key)
print("fernet_object", type(fernet_object), fernet_object)

message = "Hello, World! - سلام دنیا"
print("message", type(message), len(message), message)

message_bytes = message.encode()
print("message_bytes", type(message_bytes), len(message_bytes), message_bytes)

# token / cypher

token = fernet_object.encrypt(data=message_bytes)
print("token", type(token), len(token), token)

message_bytes = fernet_object.decrypt(token=token)
print("message_bytes", type(message_bytes), len(message_bytes), message_bytes)

message = message_bytes.decode()
print("message", type(message), len(message), message)
# ********************

print("." * 50)
