def calculator():
    print("Please enter number")
    x = float(input())
    
    print("Enter another number")
    y = float(input())
    
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    operation = input()
    
    if operation == '1':
        result = x + y
    elif operation == '2':
        result = x - y
    elif operation == '3':
        result = x * y
    elif operation == '4':
        if y != 0:
            result = x / y
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation selected"
    
    return f"Result: {result}"

# Run the calculator
print(calculator())
