###Calculator using class and object(oop) with unlimited input with exception (final)

class calculator:
    def add(self, a, b):
        return a+b
    def sub(self, a, b):
        return a-b
    def mul(self, a, b):
        return a*b
    def div(self, a, b):
        if b == 0:
            raise ZeroDivisionError("zero not allow")
        return a/b
    def modulus(self, a, b):
        return a%b

ca = calculator()

      #user defined exception
class InvalidOperatorError(Exception):
    pass

try:
    n1 = float(input("Enter first input: "))
    while True:
        try:
            op = input("Enter Operator (+, -, *, /, %) and '=' to finish: ")
            if op == "=":
                break

            if op not in ["+", "-", "*", "/", "%"]:
                raise InvalidOperatorError("Invalid Operator")

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
                res = ca.div(n1, n2)

            n1 = res

            print("Current Result: ", res)

        except ZeroDivisionError as e:
            print("Error", e)
            print("Enter num without zero")
        except ValueError as e:
            print("Error", e)
        except InvalidOperatorError as e:
            print("Error", e)
            print("Enter right operator \n")
    print("Final result: ",res)

except ValueError as e:
    print("Error: Enter right value")