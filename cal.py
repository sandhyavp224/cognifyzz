def cal(x, y):
    
    choice = input("Choose an operation( +, -, *, /): ")
    if choice == "+":
        result = x + y
        return f"You have choosen a Addition operation and the values are {x} and {y}.  the result is  {int(result)}"
    elif choice == "-":
        result = x - y
        return f"You have choosen a Subtraction operation and the values are {x} and {y}. the result is {int(result)}"
    elif choice == "*":
        result = x * y
        return f"You have choosen a Multiplication operation and the values are {x} and {y}. the result is {int(result)}"
    elif choice == "/":
        if y != 0:
            result = round(x / y, 2)
            return f"You have choosen a Division operation and the values are {x} and {y}. the result is {int(result)}"
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Invalid operation. Please choose from +, -, *, /."

val1 = float(input("Enter a value1: "))
val2 = float(input("Enter a value2: "))
print(cal(val1, val2))
    