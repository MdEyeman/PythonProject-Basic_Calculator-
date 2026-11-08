###Calculator using class and object with unlimited input 
class calculator:
    def add(self, a, b):
        return a+b
    def sub(self, a, b):
        return a-b
    def mul(self, a, b):
        return a*b
    def div(self, a, b):
        return a/b
    def modulus(self, a, b):
        return a%b
        
ca = calculator()

n1 = float(input("Enter first input: "))

while True:
    op = input("Enter Operator (+, -, *, /, %) and '=' to finish: ")
    if op == "=":
        break
    
    n2 = float(input("Enter second input: "))
    
    if op == "+":
        res = ca.add(n1, n2)
        
    elif op == "-":
        res = ca.sub(n1, n2)
    elif op == "*":
        res = ca.mul(n1, n2)
    elif op == "%":
        res = ca.modulus(n1, n2)
    elif op == "/":
        if n2 == 0:
            print("zero not allowed for divite")
        continue
        res = ca.div(n1, n2)
    else:
        print("Invalid input!")
        continue
    print("Result: ",res)
print("final result:", res)