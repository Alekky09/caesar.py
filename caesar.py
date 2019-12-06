from cs50 import get_string
from sys import argv

if len(argv) != 2:
    exit("Usage: python caesar.py k")

k = int(argv[1])

if k > 26:
    k = k % 26

print(k)
print("plaintext:", end = "")
pt = get_string(" ")
print("ciphertext: ", end = "")

for char in pt:

    if char.isalpha():
        char = chr(ord(char) + k)

        if not char.isalpha():
            char = chr(ord(char) - 26)

    print(char, end="")
print("")





