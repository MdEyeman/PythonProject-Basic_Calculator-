def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a,b):
    if b == 0:
        print("Invalid input. Please give input more than zero")
    return a/b
n1 = float(input("Enter num1: "))
op = input("Enter Operator (+, -, *, /): ")
n2 = float(input("Enter num2: "))
if op == "+":
    res = add(n1, n2)
elif op == "-":
    res = sub(n1, n2)
elif op == "*":
    res = mul(n1, n2)
elif op == "/":
    res = div(n1, n2)
else:
    print("Invalid input!")
print("Result: ",res)