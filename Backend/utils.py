import hashlib

'''
This file is for generating or verifying hased password
'''

def hash_password(password: str) -> str:
    hash_password = hashlib.sha256(password.encode()).hexdigest()
    return hash_password

def verify_password(input_password: str, stored_hash: str) -> bool:
    if hash_password(input_password) == stored_hash:
        return True
