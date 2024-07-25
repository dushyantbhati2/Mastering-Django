from cryptography.fernet import Fernet
from django.conf import settings
from dotenv import load_dotenv
load_dotenv()
import os

FERNET_KEY = os.environ.get('FERNET_KEY')
fernet = Fernet(FERNET_KEY)




def encrypt_data(data):
    encrypted_data = fernet.encrypt(data.encode()).decode()
    return encrypted_data

def decrypt_data(data):
    decrypted_data = fernet.decrypt(data.encode()).decode()
    return decrypted_data
