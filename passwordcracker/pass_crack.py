import hashlib

user_hash_dict={}

with open("com_pass.txt","r",encoding="utf-8")as f:
    com_pas=f.read().splitlines()

with open("list_data.txt","r",encoding="utf-8")as f:
    text=f.read().splitlines()
    for user_hash in text:
        name=user_hash.split(":")[0]
        hashe=user_hash.split(":")[1]
        user_hash_dict[name]=hashe

for password in com_pas:
    hashed_pas=hashlib.sha256(password.encode("utf-8")).hexdigest()

    for name,hashe in user_hash_dict.items():
        if hashed_pas==hashe:
            print(f"Hash Found:\n \t {name} : {password} \n " )