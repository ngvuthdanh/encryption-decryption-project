from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved to 'key.key'.")
    
def load_key():
    try:
        with open("key.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        print("Key file not found. Please generate a key first using 'generate_key()'.")
        return None

def encrypt_message(message):
    key = load_key()
    if key is None:
        return None

    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message):
    key = load_key()
    if key is None:
        return None

    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message

if __name__ == "__main__":
    print("1. Generate Key")
    print("2. Encrypt Message")
    print("3. Decrypt Message")
    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        generate_key()
    elif choice == "2":
        message = input("Enter the message to encrypt: ")
        encrypted = encrypt_message(message)
        if encrypted:
            print("Encrypted Message:", encrypted.decode())
    elif choice == "3":
        encrypted_message = input("Enter the encrypted message: ")
        try:
            decrypted = decrypt_message(encrypted_message.encode())
            if decrypted:
                print("Decrypted Message:", decrypted)
        except Exception as e:
            print("Failed to decrypt message. Ensure the correct key is used.")
            print("Error:", e)
    else:
        print("Invalid choice. Exiting.")
