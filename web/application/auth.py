import base64
import binascii
import hashlib
import os 

def create_salt():
    salt = base64.b64encode(os.urandom(64)).decode()
    return salt

def create_hash(password, salt):
    temp_password = hashlib.pbkdf2_hmac("sha512", password.encode('utf-8'), salt.encode('utf-8'), 100000)
    hash_password = binascii.hexlify(temp_password).decode()
    return hash_password


if __name__ == "__main__":
    salt = create_salt()
    # salt = "koR54sfR472wsdr0ol5TYdGhEfcm"
    password = '0o9i8u7y6t'
    hash_password = create_hash(password, salt)
    print('----salt-----')
    print(salt)
    print('-----hash_password-----')
    print(hash_password)