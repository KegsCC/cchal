PASSWORD = "hunter2"
attempt_plural = "s"

for i in range(10):
    if i == 9:
        attempt_plural = ""
    if i > 0:
        print(f"Wrong password. Please try again. You have {10-i} attempt{attempt_plural} left.")
    if input("Enter password: ") == PASSWORD:
        print("Welcome back!")
        break