from cryptography.fernet import Fernet

def generate_key(file_path = "encryption_key.key"):
    key = Fernet.generate_key()
    with open("file_path", "wb") as key_file: #b for :Binary format instead of text
        key_file.write(key)

    print("Key generated and saved to", file_path)     

def load_key(file_path = "encryption_key.key"):
    with open(file_path, "rb") as key_file:
        key = key_file.read()   
    return key   

def encrypt_file(input_file,output_file, key):
    fernet = Fernet(key)
    with open(input_file, "rb") as file:
        original = file.read()
        encrypted = fernet.encrypt(original)
        with open(output_file, "wb") as file:
            file.write(encrypted)