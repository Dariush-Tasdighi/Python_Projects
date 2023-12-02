""" Learn 1 """

# ********************
# Test:
# python app_01.py arg1 arg2 arg3
# ********************
import sys

for arg in sys.argv:
    print(arg)
# ********************

# ********************
# Test:
# python app_01.py
# Test:
# python app_01.py c:\Temp
# ********************
# import sys

# if len(sys.argv) < 2:
#     print("[!] You did not specify path!")
# else:
#     path = sys.argv[1]
#     print("Path:", path)
# ********************

# ********************
# Test:
# python app_01.py
# Test:
# python app_01.py c:\Temp
# ********************
# import sys

# if len(sys.argv) < 2:
#     print("[!] You did not specify path!")
#     quit()
#     # exit()

# path = sys.argv[1]
# print("Path:", path)
# ********************
