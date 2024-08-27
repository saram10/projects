import hashlib

password="12345678"

hash_v=hashlib.sha256(password.encode('utf-8'))
print("hash is: ",hash_v.hexdigest())