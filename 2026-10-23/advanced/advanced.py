attempt_plural = "s"
with open("PASSWORD.txt", encoding="utf-8") as f: # default mode is r
    password = f.readline().removesuffix("\n") # not strictly necessary but

for i in range(10):
    if i == 9:
        attempt_plural = ""
    if i > 0:
        print(f"Wrong password. Please try again. You have {10-i} attempt{attempt_plural} left.")
    if input("Enter password: ") == password:
        print("Welcome back!")
        break