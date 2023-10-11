import os
from cryptography import fernet

files, i = os.listdir(), 0

while i < len(files):
    if files[i] in ("virus.py", "secret.key", "antivirus.py", ".git"):files.pop(i)
    elif os.path.isdir(files[i]):
        for j in os.listdir(files[i]):files.append(f"{files[i]}/{j}")
        files.pop(i)
    else:i += 1

with open("secret.key", "rb") as secret:
    key = secret.read()

for file in files:
    if os.path.isdir(file):continue
    else:
        with open(file, "rb") as data:
            data = data.read()
            data = fernet.Fernet(key).decrypt(data)
        # try:
        with open(file, "w") as victim:
            print(data)
            victim.write(data.decode())
        # except:pass

print("The following files has been recovered---")
for file in files:print(file)