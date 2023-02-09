"""
Project 1: Encryption and Decryption using Caesar Cipher.
Getting input 'text' and 'key' from user and showing output.
"""

print("Hey, This is a demo project for encryption/decryption of text provided.")
text = input("Type in the Text you want to encrypt:\n")
key = int(input("Provide a key:\n"))
x = text
k = key
s = []
p = []
for a in x:
    s.append(chr(ord(a) + k))

e = ''.join(map(str, s))
print("Encrypted value is:", e)
ask = input("Do you want to Decrypt: Type y/n\n")
if ask == "y":
    k2 = int(input("Provide the Key:"))
    for b in e:
        p.append(chr(ord(b) - k2))

    d = ''.join(map(str, p))
    print("Decrypted value is:", d)
else:
    print("Thank for your time.")