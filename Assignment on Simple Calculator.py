# 1. ADD
# 2. SUBTRACT
# 3. MULTIPLY
# 4. DIVIDE

print("Select an operation to perform:")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

operation = input()
if operation == "1":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"The sum is {int(num1) + int(num2)}")
    pass
elif operation == "2":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"The difference is {int(num1) - int(num2)}")
    pass
elif operation == "3":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"The product is {int(num1) * int(num2)}")
    pass
elif operation == "4":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"The quotinet is  {int(num1) / int(num2)}")
else:
    print("Invalid Entry")
