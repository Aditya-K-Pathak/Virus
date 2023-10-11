from cryptography.fernet import Fernet
"""
A module particularly build for all operations related to 
Encrption Decryption and Key Generation
"""

class Cryptograph:

    def __init__(self) -> None:
        self.key = ""

    def create_key(self) -> None:
        """
        A funtion that generates a key for encryption
        :params - None
        :return - None
        """
        if self.key != "":return
        self.key = Fernet.generate_key()
        with open("key.key", "wb") as secret:
            secret.write(self.key)
        return self.key

    def read_key(self) -> bytes:
        """
        A function that reads data from key file, 
        basically meant for decryption
        :params - None
        :return - bytes
        """
        with open("key.key", "rb") as secret:
            self.key = secret.read()
        return self.key
    
    def encrypt(self, content: str) -> bytes:
        """
        A funtion that encrypt the content and returns it byte form
        :params - str -> The data to be encrypted
        :return - bytes -> Encrypted data as bytes
        """
        if self.key == "":self.create_key()
        return Fernet(self.key).encrypt(content.encode())
    
    def decrypt(self, content: bytes) -> str:
        """
        A function that decrypt the data and return it as string
        :params - content -> Encrypted data
        :return - str -> decoded string
        """
        self.key = self.read_key()
        return Fernet(self.key).decrypt(content)
    