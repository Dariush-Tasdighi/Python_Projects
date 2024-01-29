# ********************
# فلسفه هر چیزی از خود آن چیز مهم‌تر است
# ********************

# ********************
# Binary / Text (ASCII or Unicode) <- Base64 (Algorithm) -> Plain Text (ASCII) (33% Larger!!!)
# ********************

# ********************
# https://en.wikipedia.org/wiki/Base64
# http://sticksandstones.kstrom.com/appen.html
# ********************
# https://www.base64encode.org
# https://www.base64decode.org
# https://base64.guru/converter/encode/text
# https://onlinestringtools.com/convert-string-to-base64
# ********************

# ********************
# کاربردها
#
# به طور خلاصه انتقال / ذخیره داده، به صورت متنی
# ********************

# ********************
# (1)
# Json:
#
# {
#   "age" : 50,
#   "fullName" : "Dariush Tasdighi",
#   "picture" : ?????
# }
#
# (2)
# XML:
#
# <person>
#   <age>50</age>
#   <fullName>Dariush Tasdighi</fullName>
#   <picture>?????</picture>
# </person>
#
# (3)
# Hashing
#
# (4)
# URL Parameters
# www.x.com/list?x=1&y=2&token=asfafsf24234sfasdfasdfas2423
#
# (5)
# HTML:
# <img src="?????">
# <input type="hidden" value="?????">
#
# (6)
# Email Attachment
# ********************

# ********************
# Ali => Binary
# ********************
#                            1
#   1 Bit                   2       = 2                             Bit
#
#                            4
#   4 Bits                  2       = 16                            Nybble
#
#                            8
#   8 Bits / 1 Byte         2       = 256                           Byte
#
#                            16
#   16 Bits / 2 Bytes       2       = 65_536                        Word
#
#                            32
#   32 Bits / 4 Bytes       2       = 4_294_967_296                 Long Word
#
#                            64
#   64 Bits / 4 Byte        2       = 18_446_744_073_709_551_616    Very Long Word
# ********************

# ********************
# [ASCII]
#
# ASCII was the first major encoding
#   Because of computer limitations it was only 1 byte
# ASCII is American Standard Code for Information Interchange
# ASCII is a character encoding
#   - Maps some bits (0's and 1's) into characters
#   - Uses 7 bits for encoding, meaning it can represent
#      7
#   - 2 = 128 different characters
#   - The original 7 bits were only enough to represent
#       English characters and punctuation
#   - Since a byte is 8 bits, there was a lot of
#       competition on which other characters should be supported
#
# Example:
#   - A ->  65   ->    1000001 (7 bits)   ->  01000001 (8 bits)
#   - t ->  116  ->    1110100 (7 bits)   ->  01110100 (8 bits)
# ********************

# ********************
# [Unicode]
#
# Unicode is a universal character encoding
#   - Supports many different alphabets and even emojis
#   - Unlike ASCII, Unicode does not define how its mapping
#        should be implemented
#   - Only specifies which character refers to which code point
#       - Code point is a hexadecimal number representing a character
#           Example: U+0041 => A
#   - Unicode was invented to address the problem of encoding
#        more languages than just English
# ********************

# ********************
# [UTF-8]
#
#   - UTF stands for Unicode transformation format
#       - Algorithmic mapping from every Unicode code point to
#           a unique byte sequence
#   - UTF-8 has variable length encoding
#       - Characters with code points with small values (like A)
#           can be represented with just one byte!
#   - Backward compatible with ASCII
#   - UTF-8 is not the dominant encoding for the World Wide
#       Web and accounts for roughly 98% of all web pages
#   - UTF-8 is a variable length encoding that is backwards
#       compatible with ASCII and is the most popular encoding today
# ********************

# ********************
# Example:
#
#   Character           Code Point          UTF-8 Binary Encoding
#
#   A                   U+0041              01000001
#   t                   U+0074               1110100
#   یک حرف چینی        U+29D5A             11110000    10101001
#                                           10110101    10011010 (4 Bytes)
# ********************

# ********************
#       6
# 64 = 2
# ********************

# ********************
import os

os.system(command="cls")
# ********************

print("." * 50)

# ********************
char = "A"
print("char", type(char), char)

char_ord = ord(char)
print("char_ord", type(char_ord), char_ord)

char_binary = bin(char_ord)
print("char_binary", type(char_binary), char_binary)

char_ord = int(char_binary, base=2)
print("char_ord", type(char_ord), char_ord)

char = chr(char_ord)
print("char", type(char), char)
# ********************

print("." * 50)

# ********************
print("A:", bin(ord("A")))
print("l:", bin(ord("l")))
print("i:", bin(ord("i")))
# ********************
print("ع:", bin(ord("ع")))
print("ل:", bin(ord("ل")))
print("ی:", bin(ord("ی")))
# ********************

# ********************
# Ali
#
# A         l           i
#
# 1000001   1101100     1101001
#
# 01000001  01101100    01101001
#
# 010000010110110001101001
#
# 010000 010110 110001 101001
# Q      W      x      p
#
# QWxp
# ********************

# ********************
# 0     ...     25
# A     ...     Z       Uppercase Letters
#
# 26    ...     51
# a     ...     z       Lowercase Letters
#
# 52    ...     61
# 0     ...     9       Digits
#
# 62    AND     63
# +     ...     /       Symbols
#
# =                     Just Padding (=) OR (==)
# ********************

# ********************
# Hello
# SGVsbG8=
# ********************

# ********************
# What is '='?
# بعد از آن‌که شش‌تا شش‌تا جدا کردیم
# 111111
# 1111      => 1111[00]   => =
# 11        => 11[0000]   => ==
# ********************

# ********************
# In Linux:
#
#   > echo 'Hello World'
#   Hello World
#
#   > echo 'Hello World' | base64
#   SGVsbG8gV29ybGQK
#
#   > echo 'Hello World' | base64 | base64 --decode
#   Hello World
#
#   > SGVsbG8g[!!]V29ybGQK | base64 --decode
#   Hello W Invalid Character!
#
#   > SGVsbG8g[!!]V29ybGQK | base64 --decode -i
#   Hello World
#
# Note: -i => Ignore Invalid Characters!
# ********************

# ********************
# In Linux:
#
# > show user local
#   Password: Hashed by SHA-256 -> Base64
# ********************
