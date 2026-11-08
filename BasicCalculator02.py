###Calculator using class, object
class calculator:
    def add(self, a, b):
        return a+b
    def sub(self, a, b):
        return a-b
    def mul(self, a, b):
        return a*b
    def div(self, a,b):
        if b == 0:
            print("Invalid input. Please give input more than zero")
        return a/b

ca = calculator()

n1 = float(input("Enter num1: "))
op = input("Enter Operator (+, -, *, /): ")
n2 = float(input("Enter num2: "))
if op == "+":
    res = ca.add(n1, n2)
elif op == "-":
    res = ca.sub(n1, n2)
elif op == "*":
    res = ca.mul(n1, n2)
elif op == "/":
    res = ca.div(n1, n2)
else:
    print("Invalid input!")
print("Result: ",res)
