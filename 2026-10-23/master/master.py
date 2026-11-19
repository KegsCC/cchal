from getpass import getpass
import json
import os

DBPATH = "master_db.json"
data: dict[str, str]
if not os.path.exists(DBPATH):
    with open(DBPATH, "w") as f:
        f.write("{}")
with open(DBPATH) as f:
    data = json.load(f)
attempt_plural = "s"

def successful_login(user):
    if input("Create account (y/n): ").strip().lower() == "y":
        new_username = input("Enter username: ")
        if new_username in data:
            print("Username already in use")
            successful_login(user)
        new_password = getpass("Enter password (hidden prompt): ")
        data[new_username] = new_password
    if input("Change your password (y/n): ").strip().lower() == "y":
        new_password = getpass("Enter new password (hidden prompt): ")
        data[username] = new_password

for i in range(10):
    if i == 9:
        attempt_plural = ""
    if i > 0:
        print(f"Wrong username or password. Please try again. You have {10-i} attempt{attempt_plural} left.")
    username = input("Username: ")
    password = getpass("Enter password (hidden prompt): ")
    if username in data and password == data[username]:
        successful_login(username)
        break

with open(DBPATH, "w") as f:
    json.dump(data, f)