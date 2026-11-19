import base64
from getpass import getpass
import json
import os
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives.kdf.argon2 import Argon2id

DBPATH = "supreme_db.json"
data: dict[str, str]

def change_details(username, password, program):
    kdf = Argon2id(salt=b"6767"*16, length=32, iterations=1, lanes=4, memory_cost=2**20)
    key = base64.urlsafe_b64encode(kdf.derive((username+password).encode()))
    data[username] = { "program": Fernet(key).encrypt(program.encode()).decode() }
    with open(DBPATH, "w") as f:
        json.dump(data, f)
    print("Details saved successfully!")

def login(username, password):
    print("Attempting login, please standby...") # T-5, T-4, T-3, T-2, T-1, Kablooey!
    kdf = Argon2id(salt=b"6767"*16, length=32, iterations=1, lanes=4, memory_cost=2**20)
    key = base64.urlsafe_b64encode(kdf.derive((username+password).encode()))
    try:
        code = Fernet(key).decrypt(data[username]["program"]).decode()
        vars = {
            "__builtins__": __builtins__,
            "change_details": change_details,
            "code": code,
            "username": username,
            "password": password,
        }
        exec(code, vars, vars)
        return True
    except InvalidToken:
        return False

if not os.path.exists(DBPATH):
    with open(DBPATH, "w") as f:
        f.write("{}")
with open(DBPATH) as f:
    data = json.load(f)
attempt_plural = "s"

for i in range(10):
    if i == 9:
        attempt_plural = ""
    if i > 0:
        print(f"Wrong password. Please try again. You have {10-i} attempt{attempt_plural} left.")
    username = input("Username: ")
    password = getpass("Enter password (hidden prompt): ")
    if login(username, password) == True:
        break