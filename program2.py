from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

key = RSA.import_key(open("public.key").read())

with open("signed_file.pdf", "rb") as file_signed:
    message = file_signed.read()
    file_signed.close()

with open("signature.pem", "rb") as file_signature:
    signature = file_signature.read()
    file_signature.close()

h = SHA256.new(message)

try:
    pkcs1_15.new(key).verify(h, signature)
    print("Signature is valid")
except(ValueError, TypeError):
    print("Signature is not valid")