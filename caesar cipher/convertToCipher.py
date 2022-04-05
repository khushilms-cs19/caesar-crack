plaintext = input("Enter the plain text: ")
cipher = ""
for ch in plaintext:
    cipher += chr(ord(ch)+3)
print("The cipher is : ", cipher)