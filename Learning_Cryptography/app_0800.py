print("." * 50)

# ********************
import base64
import hashlib
from cryptography.fernet import Fernet

password = input("Password: ")
print("password", type(password), len(password), password)

password_bytes = password.encode()
print("password_bytes", type(password_bytes), len(password_bytes), password_bytes)

md5_hashed_password_object = hashlib.md5(password_bytes)
print(
    "md5_hashed_password_object",
    type(md5_hashed_password_object),
    md5_hashed_password_object,
)

md5_hashed_password = md5_hashed_password_object.hexdigest()
print(
    "md5_hashed_password",
    type(md5_hashed_password),
    len(md5_hashed_password),
    md5_hashed_password,
)

md5_hashed_password_bytes = md5_hashed_password.encode()
print(
    "md5_hashed_password_bytes",
    type(md5_hashed_password_bytes),
    len(md5_hashed_password_bytes),
    md5_hashed_password_bytes,
)

# Note: Fernet key must be 32 url-safe base64-encoded
key = base64.urlsafe_b64encode(s=md5_hashed_password_bytes)
print("key", type(key), len(key), key)

fernet_object = Fernet(key=key)
print("fernet_object", type(fernet_object), fernet_object)

message = "Hello, World! - سلام دنیا"
print("message", type(message), len(message), message)

message_bytes = message.encode()
print("message_bytes", type(message_bytes), len(message_bytes), message_bytes)

token = fernet_object.encrypt(data=message_bytes)
print("token", type(token), len(token), token)

message_bytes = fernet_object.decrypt(token=token)
print("message_bytes", type(message_bytes), len(message_bytes), message_bytes)

message = message_bytes.decode()
print("message", type(message), len(message), message)
# ********************

print("." * 50)
