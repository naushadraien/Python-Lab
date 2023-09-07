import calcEngine as calc

input_val = input("Enter values with sign: ")

input_val = input_val.split(" ")

if input_val[1] == "+":
    print("Sum: ")
    calc.sum(int(input_val[0]), int(input_val[2]))
elif input_val[1] == "-":
    print("Sub: ")
    calc.sub(int(input_val[0]), int(input_val[2]))
elif input_val[1] == "*":
    print("Mul: ")
    calc.mul(int(input_val[0]), int(input_val[2]))
elif input_val[1] == "/":
    print("Div: ")
    calc.div(int(input_val[0]), int(input_val[2]))
