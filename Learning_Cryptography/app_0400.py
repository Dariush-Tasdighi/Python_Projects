# ********************
import os

os.system(command="cls")
# ********************

print("." * 50)
print("Step (1)")
print("." * 50)

# ********************
# Note
import base64

key_string = "Ali"
print("key_string:", type(key_string), len(key_string), key_string)

key_bytes = key_string.encode()
print("key_bytes:", type(key_bytes), len(key_bytes), key_bytes)

# Note
key_base64_bytes = base64.b64encode(s=key_bytes)
print("key_base64_bytes:", type(key_base64_bytes), len(key_base64_bytes), key_base64_bytes)

key_base64_string = key_base64_bytes.decode()
print("key_base64_string:", type(key_base64_string), len(key_base64_string), key_base64_string)

# Note
key_bytes = base64.b64decode(s=key_base64_bytes)
# OR
key_bytes = base64.b64decode(s=key_base64_string)
print("key_bytes:", type(key_bytes), len(key_bytes), key_bytes)

key_string = key_bytes.decode()
print("key_string:", type(key_string), len(key_string), key_string)
# ********************

print("." * 50)
print("Step (2)")
print("." * 50)

# ********************
import base64

key_string = "Ali"
print("key_string:", type(key_string), len(key_string), key_string)

key_bytes = key_string.encode()
print("key_bytes:", type(key_bytes), len(key_bytes), key_bytes)

# Note
key_base64_bytes = base64.urlsafe_b64encode(s=key_bytes)
print("key_base64_bytes:", type(key_base64_bytes), len(key_base64_bytes), key_base64_bytes)

key_base64_string = key_base64_bytes.decode()
print("key_base64_string:",type(key_base64_string), len(key_base64_string),key_base64_string)

# Note
key_bytes = base64.urlsafe_b64decode(s=key_base64_bytes)
# OR
key_bytes = base64.urlsafe_b64decode(s=key_base64_string)
print("key_bytes:", type(key_bytes), len(key_bytes), key_bytes)

key_string = key_bytes.decode()
print("key:", type(key_string), len(key_string), key_string)
# ********************

print("." * 50)
print("Step (3)")
print("." * 50)

# ********************
import base64

key_string = "علی"
print("key_string:", type(key_string), len(key_string), key_string)

key_bytes = key_string.encode()
print("key_bytes:", type(key_bytes), len(key_bytes), key_bytes)

# Note
key_base64_bytes = base64.b64encode(s=key_bytes)
print("key_base64_bytes:", type(key_base64_bytes), len(key_base64_bytes), key_base64_bytes)

key_base64_string = key_base64_bytes.decode()
print("key_base64_string:", type(key_base64_string), len(key_base64_string), key_base64_string)

# Note
key_bytes = base64.b64decode(s=key_base64_bytes)
# OR
key_bytes = base64.b64decode(s=key_base64_string)
print("key_bytes:", type(key_bytes), len(key_bytes), key_bytes)

key_string = key_bytes.decode()
print("key_string:", type(key_string), len(key_string), key_string)
# ********************

print("." * 50)
print("Step (4)")
print("." * 50)

# ********************
import base64

key_string = "علی"
print("key_string:", type(key_string), len(key_string), key_string)

key_bytes = key_string.encode()
print("key_bytes:", type(key_bytes), len(key_bytes), key_bytes)

# Note
key_base64_bytes = base64.urlsafe_b64encode(s=key_bytes)
print("key_base64_bytes:", type(key_base64_bytes), len(key_base64_bytes), key_base64_bytes)

key_base64_string = key_base64_bytes.decode()
print("key_base64_string:", type(key_base64_string), len(key_base64_string), key_base64_string)

# Note
key_bytes = base64.urlsafe_b64decode(s=key_base64_bytes)
# OR
key_bytes = base64.urlsafe_b64decode(s=key_base64_string)
print("key_bytes:", type(key_bytes), len(key_bytes), key_bytes)

key_string = key_bytes.decode()
print("key:", type(key_string), len(key_string), key_string)
# ********************

print("." * 50)
print("Next Lession...")
print("." * 50)

# ********************
print("See convert_to_base64.py")
print("See convert_from_base64.py")
# ********************

print("." * 50)
