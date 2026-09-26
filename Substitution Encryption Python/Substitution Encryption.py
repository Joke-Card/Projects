
import string
import random
import json
import os

characters= " " + "¬" + string.punctuation + string.digits + string.ascii_letters
characters = list(characters)

KEY_FILE = "key.json"

if os.path.exists(KEY_FILE):
    with open(KEY_FILE, "r")as file:
        key = json.load(file)

else:
    key = characters.copy()
    random.shuffle(key)

    with open(KEY_FILE, "w")as file:
        json.dump(key, file)

#Encryption Phase
def encryption():
    text = input("\nEnter text to encrypt: ")
    cipher = ""

    for letter in text:
        index = characters.index(letter)
        cipher += key[index]

    print(f"\nPlain text: {text}")
    print(f"Encrypted text: {cipher}")


#Decryption Phase
def decryption():
    cipher = input("\nEnter text to decrypt: ")
    text = ""

    for letter in cipher:
        index = key.index(letter)
        text += characters[index]

    print(f"\nEnrypted text: {cipher}")
    print(f"Plain text: {text}")


print("=========Substitution=========")
print("")
print("1. I would like to encrypt text")
print("2. I would like to decrypt text")
print("3. I would like to quit.")

flag = True
while flag:
    num = input("\nEnter the numbered task you want: ")
    if num == "1":
        encryption()

    elif num == "2":
        decryption()

    elif num == "3":
        flag = False

    else:
        print("You did not enter either 1, 2 or 3")
