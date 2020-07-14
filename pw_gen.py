import os
import os.path
import string
import time
from os import listdir
from os.path import isfile, join
from random import choice, randint

from Crypto import Random
from Crypto.Cipher import AES

lower = string.ascii_lowercase
upper = string.ascii_uppercase
letters = string.ascii_letters
chars = letters + string.digits+string.punctuation 

def caesar(message,command,key):
    #encrypt
    #key = int(input("Enter key value "))
    if command == 'encrypt':
        if 0 < key < 26: 
            encrypted = ''
            for i in message.lower():
                if i in lower:
                    char_ind = lower.index(i)
                    encrypted+= lower[(char_ind + key)%len(lower)]
                else: #is not a letter
                    encrypted+= i
            return encrypted
        else: return "Key is out of range"

    if command == 'decrypt':
        if 0 < key < 26: 
            decrypted = ''
            for i in message.lower():
                if i in lower:
                    char_ind = lower.index(i)
                    decrypted += lower[(char_ind - key)%len(lower)]
                else: #is not a letter
                    decrypted += i
            return decrypted
        else: return "Key is out of range"


def pw_generate(min_char):
    password = ''
    for i in range(min_char):
        password += choice(chars)
    return password

class Encryptor:
    def __init__(self,key):
        self.key = key
    def pad(self,w):
        return w + b"\0" * (AES.block_size - len(w) % AES.block_size)

    def encrypt(self,message,key,key_len = 256):
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)

    def encrypt_file(self, file_name):
        with open(file_name, 'rb') as path:
            plainttext = path.read()
        enc = self.encrypt(plainttext,self.key)
        with open(file_name + ".enc", 'wb') as path:
            path.write(enc)
        os.remove(file_name)

    def decrypt(self, ciphertext, key):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")

    def decrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            ciphertext = fo.read()
        dec = self.decrypt(ciphertext, self.key)
        with open(file_name[:-4], 'wb') as fo:
            fo.write(dec)
        os.remove(file_name)

    def getAllFiles(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dirs = []
        for dirName, subdirList, fileList in os.walk(dir_path):
            for fname in fileList:
                if (fname != 'script.py' and fname != 'data.txt.enc'):
                    dirs.append(dirName + "\\" + fname)
        return dirs

    def encrypt_all_files(self):
        dirs = self.getAllFiles()
        for file_name in dirs:
            self.encrypt_file(file_name)

    def decrypt_all_files(self):
        dirs = self.getAllFiles()
        for file_name in dirs:
            self.decrypt_file(file_name)

key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
enc = Encryptor(key)
clear = lambda: os.system('clear')


def main():
    func = str(input("Do you want to use Caesar Encryption or AES Encryption?: "))

    if func == ("Caesar" or "Caesar Encryption"):
        message = str(input("Enter message you would like to be encrypted/decrypted: "))
        command= str(input("Do you want to Encrypt or Decrypt this message: "))
        key=int(input("Choose key: "))
        print(caesar(message,command,key))
        time.sleep(5)
    
    elif func == "AES" or "AES Encryption":
        if os.path.isfile('data.txt.enc'):
            while True:
                password = str(input("Enter password: "))
                enc.decrypt_file("data.txt.enc")
                p = ''
                with open("data.txt", "r") as f:
                    p = f.readlines()
                if p[0] == password:
                    enc.encrypt_file("data.txt")
                    break

            while True:
                clear()
                choice = int(input(
                    "1. Press '1' to encrypt file.\n2. Press '2' to decrypt file.\n3. Press '3' to Encrypt all files in the directory.\n4. Press '4' to decrypt all files in the directory.\n5. Press '5' to exit.\n"))
                clear()
                if choice == 1:
                    enc.encrypt_file(str(input("Enter name of file to encrypt: ")))
                elif choice == 2:
                    enc.decrypt_file(str(input("Enter name of file to decrypt: ")))
                elif choice == 3:
                    enc.encrypt_all_files()
                elif choice == 4:
                    enc.decrypt_all_files()
                elif choice == 5:
                    exit()
                else:
                    print("Please select a valid option!")

        else:
            while True:
                clear()
                password = str(input("Setting up stuff. Enter a password that will be used for decryption: "))
                repassword = str(input("Confirm password: "))
                if password == repassword:
                    break
                else:
                    print("Passwords Mismatched!")
            f = open("data.txt", "w")
            f.write(password)
            f.close()
            enc.encrypt_file("data.txt")
            print("Please restart the program to complete the setup")
            time.sleep(15)
    else:
        print("Please Select a Valid Option ")

if __name__=='__main__':
    main()

