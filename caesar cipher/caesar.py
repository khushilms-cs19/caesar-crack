cipher = input("Enter the caesar cipher: ")
for i in range(26):
    plaintext = ""
    for ch in cipher:
        temp = (ord(ch)-i)
        if temp < 65 : 
            temp = 122 - (65-temp)
        plaintext += chr(temp)
    print(plaintext)
