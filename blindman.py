from cipher   import cipher
from decipher import decipher

menu = input("Enter your choice:\n   1. Cipher \n   2.Decipher \n    ")

if menu == '1':
    msg = input("Enter data to be ciphered here: \n   ")
    cipher(msg)
elif menu == '2':
    txtfile = input("Enter text file to be deciphered here: \n   ")
    plaintext = decipher(txtfile)
    print(plaintext)
