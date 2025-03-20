def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "No dividing by zero, homie"
        
first = float (input ("Value 1: "))
second = float (input ("Value 2: "))
operator = str (input ("Plus, Minus, Multiply, DIVIDE?"))

allowed_ops = ["+", "*", "/", "-"]

if operator not in allowed_ops:
    raise Exception (f"Mr. T Pitty da fool who try using {operator} use one of deez instead '{' , '.join(allowed_ops)}'.")
    
    
result = eval(f"{first} {operator} {second}")

print (f"Yo check this out {result}")