num1=float(input("enter the num 1:"))

num2=float(input("enter the num 2:"))

# Perform arithmetic operations
addition = num1 + num2

substraction = num1-num2

multiplication =  num1*num2

division = num1/num2 if num2 !=0 else "undefined (division by zero)"

modulus = num1%num2 if num2 !=0 else "undefined (modulus by zero)"





print(f"addition: {num1}+{num2}={addition}")

print(f"susbstraction {num1}-{num2}={substraction}")

print(f"multiplication: {num1}*{num2}{multiplication}")

print(f"division: {num1}/{num2}={division}")

print(f"modulus: {num1}% {num2}={modulus}")