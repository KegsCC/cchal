import base64
import hashlib
import json
import os
import sys
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives.kdf.argon2 import Argon2id
from getpass import getpass

DBPATH = "champion_db.json"
data: dict[str, str]

# Unfortunately, showing any more would be teaching how to make dangerous code, so we will not be doing any further than this.
def debug_check():
    # https://stackoverflow.com/questions/333995/how-to-detect-that-python-code-is-being-executed-through-the-debugger
    # https://www.reddit.com/r/pycharm/comments/1956hoi/can_a_python_app_running_on_the_debugger_know_it/
    if sys.gettrace() is not None or any(mod in sys.modules for mod in {'debugpy', 'pydevd', 'pdb'}):
        sys.exit()

    if any(flag in os.environ for flag in {"DEBUGGER_HEADER", "PYDEVD_LOAD_VALUES_ASYNC", "PYTHONBREAKPOINT"}):
        sys.exit()
        
    def debug_block(*args, **kwargs):
        return debug_block
    sys.settrace = debug_block

def file_check():
    compromised = False
    with open(__file__) as f:
        if not os.path.isfile(hashlib.sha256(f.read().encode()).hexdigest()):
            compromised = True
    if compromised:
        open(__file__, "w").close()
        sys.exit()

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

debug_check()
file_check()
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