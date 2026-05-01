# Project : Secret Message Vault 
# Author : Samiksha Rani
# Description : A privacy tool to encode and decode messages using a Caesar Cipher.

def caesar_cipher(text, shift, mode):
    result = ""
    if mode == "decode":
        shift = -shift
    
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            # The logic: Shift the character and wrap around the alphabet

            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        else:
            result += char
    return result

print("--- SECRET MESSAGE VAULT---")
msg = input("Enter your message: ")
key = int(input("Enter secret key(1-25) "))
action = input("Type 'encode' to hide or 'decode' to reveal: ").lower()

print(f"\nResult: {caesar_cipher(msg, key, action)}")