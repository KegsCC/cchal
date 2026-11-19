first_number = float(input("First number: "))
operation = input("Operation (+, -, /, *, %, //, **): ")
second_number = float(input("Second Number: "))

# Validation is not necessary here, although you could add it if you wanted to.
if operation == "+":
    print(first_number + second_number) # Implicit type casting from float to string here.
elif operation == "-":
    print(first_number - second_number)
elif operation == "/":
    print(first_number / second_number)
elif operation == "*":
    print(first_number * second_number)
elif operation == "%":
    print(first_number % second_number)
elif operation == "//":
    print(first_number // second_number)
elif operation == "**":
    print(first_number ** second_number)
else:
    print("Operation not supported.")


# A more simple, but slightly cursed way of doing it would be this. exec() also works just as well.
# eval(first_number+operation+second_number)

# This also works, hiding the cursed code by making it more cursed.
# getattr(__builtins__, bytes(byte ^ 0x67 for byte in b"\x02\x11\x06\x0b").decode())(first_number+operation+second_number)