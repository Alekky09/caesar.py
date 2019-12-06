from cs50 import get_string
from sys import argv

if len(argv) != 2:
    exit("Usage: python caesar.py k")

k = int(argv[1])

if k > 25:
    k = k % 25
print(k)
print("plaintext:", end = "")
pt = get_string(" ")

print("cyphertext: ", end = "")

for char in pt:
    if char.isalpha():
        char = chr(ord(char) + k)
    print(char, end="")
print("")




