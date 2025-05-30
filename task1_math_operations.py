num1=float(input("Enter the first number:     "))
num2=float(input("Enter the Second number:     "))

addition=num1+num2
subtraction=num1-num2
multiplication=num1*num2
division=num1/num2 if num2 !=0 else "Undefined(Division by zero)"

print("\nResults:")
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")