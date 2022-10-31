from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

def verify(message, signature):
    h = SHA256.new(message)

    try:
        pkcs1_15.new(key).verify(h, signature)
        print("Signature is valid")
    except(ValueError, TypeError):
        print("Signature is not valid")

def read():
    with open(file, "rb") as file_signed:
        message = file_signed.read()
        file_signed.close()
    
    with open(signature_file, "rb") as file_signature:
        signature = file_signature.read()
        file_signature.close()

    verify(message, signature)

key = RSA.import_key(open("public.key").read())
file = input("Enter your file that you want to verify: ")
signature_file = input("Enter your signature file name: ")

read()
