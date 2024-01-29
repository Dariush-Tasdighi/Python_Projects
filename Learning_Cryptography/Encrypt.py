# ********************
# pip install stdiomask
# ********************
import os, base64, hashlib, stdiomask
from cryptography.fernet import Fernet


def get_path_parts(path: str):
    if path == None:
        return None

    path = path.strip()

    if path == "":
        return None

    location, tail = os.path.split(p=path)

    items = os.path.splitext(p=tail)

    file_name = items[0]
    file_extension = items[1]

    parts = (location, file_name, file_extension)

    return parts


os.system(command="cls")

source_path = input("File for encryption: ")

source_path = source_path.strip()
if source_path == "":
    print(f"[!] You did not specify file!")
    quit()

if os.path.exists(path=source_path) == False:
    print(f"[!] File '{source_path}' does not exist!")
    quit()

if os.path.isfile(path=source_path) == False:
    print(f"[!] '{source_path}' is not file!")
    quit()

password = stdiomask.getpass(prompt="Password: ", mask="")
password_bytes = password.encode()

md5_hashed_password_object = hashlib.md5(password_bytes)
md5_hashed_password = md5_hashed_password_object.hexdigest()
md5_hashed_password_bytes = md5_hashed_password.encode()

# Note: Fernet key must be 32 url-safe base64-encoded
key = base64.urlsafe_b64encode(s=md5_hashed_password_bytes)

fernet_object = Fernet(key=key)

with open(file=source_path, mode="rb") as file_object:
    message = file_object.read()

# نیازی به دستور ذیل نیست
# باز شده است binnary چرا که فایل به صورت
# message_bytes = message.encode()

token = fernet_object.encrypt(data=message)

source_path_parts = get_path_parts(path=source_path)
location = source_path_parts[0]
if location != "":
    target_path = f"{location}\\"

target_path = f"{location}{source_path_parts[1]}.enc"

with open(file=target_path, mode="wb") as file:
    file.write(token)

print("Finished...")
print("." * 50)
# ********************
