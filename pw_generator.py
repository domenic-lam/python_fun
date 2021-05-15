# Password Generator

import random

chars = "abcdefghijklmnopqrstuvwxyz"
nums = "1234567890"
# misc = "!@#%&"


pw_len = int(input("How long should the password be? "))

pw = ""

for i in range(1, pw_len):
    if i % 3 == 0:
        pw += random.choice(nums)
    elif i % 5 == 0:
        pw += "-"
    else:
        pw += random.choice(chars)

print("Password: " + pw)