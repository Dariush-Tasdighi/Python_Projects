print("." * 50)

# ********************
import base64
from cryptography.fernet import Fernet

# Note: Fernet key must be 32 url-safe base64-encoded
# password = "Hello"
password = "01234567890123456789012345678901"
print("password", type(password), len(password), password)

password_bytes = password.encode()
print("password_bytes", type(password_bytes), len(password_bytes), password_bytes)

# key = Fernet.generate_key()
key = base64.urlsafe_b64encode(s=password_bytes)
fernet_object = Fernet(key=key)
print("fernet_object", type(fernet_object), fernet_object)

message = "Hello, World! - سلام دنیا"
print("message", type(message), len(message), message)

message_bytes = message.encode(encoding="utf-8")
print("message_bytes", type(message_bytes), len(message_bytes), message_bytes)

token = fernet_object.encrypt(data=message_bytes)
print("token", type(token), len(token), token)

message_bytes = fernet_object.decrypt(token=token)
print("message_bytes", type(message_bytes), len(message_bytes), message_bytes)

message = message_bytes.decode()
print("message", type(message), len(message), message)
# ********************

print("." * 50)
