# To create and sign a document
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

def generate_key():
    key = RSA.generate(2048)
    private_key = key.export_key()

    with open("private.key", "wb") as file_prkey:
        file_prkey.write(private_key)
        file_prkey.close()

    public_key = key.publickey().export_key()

    with open("public.key","wb") as file_pkey:
        file_pkey.write(public_key)
        file_pkey.close()

def sign_file(private_key, file_name):
    with open(private_key, "rb") as file_key:
        readprv_key = file_key.read()
    
    with open(file_name, "rb") as file_message:
        file_readed = file_message.read()

    key = RSA.import_key(readprv_key)
    h = SHA256.new(file_readed) # hash 
    signer = pkcs1_15.new(key)
    signature = signer.sign(h)

    with open("signature.pem", "wb") as file_signature:
        file_signature.write(signature)
        file_signature.close()
    
    with open("signed_file.pdf", "wb") as file_signed:
        file_signed.write(file_readed)
        file_signed.close()

def check_command(command):
    if command == 'n' or command == 'N':
        generate_key()

        private_key = "private.key" 
        file_name = input("Input your file that wanted to sign: ")
        sign_file(private_key, file_name)

    elif command == 'y' or command == 'Y':
        private_key = input("Input your private key file name: ")
        file_name = input("Input your file that wanted to sign: ")
        sign_file(private_key, file_name)

    else:
        print("command not found")
    
command = input("Enter 'y' if you have a key or enter 'n' if you don't have one: ")
check_command(command)
print("File successfully signed!")
