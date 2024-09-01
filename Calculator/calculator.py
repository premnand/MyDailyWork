def calculate(expression):
    try:
        # Evaluate the expression using the eval function
        result = eval(expression, {"__builtins__": None}, {})
        return result
    except SyntaxError:
        return "Error: Invalid syntax in the expression."
    except NameError:
        return "Error: Invalid characters or variables used."
    except ZeroDivisionError:
        return "Error: Division by zero."
    except Exception as e:
        return f"Error: {e}"

def main():
    print("Simple Calculator")
    print("Type 'exit' to quit")
    print("Type 'history' to view past calculations")
    
    history = []  # List to store history of calculations
    
    while True:
        user_input = input("Enter a calculation (e.g., 2+2): ")
        
        if user_input.lower() == 'exit':
            print("Exiting the calculator.")
            break
        elif user_input.lower() == 'history':
            if history:
                print("Calculation History:")
                for entry in history:
                    print(entry)
            else:
                print("No history available.")
        else:
            result = calculate(user_input)
            history.append(f"{user_input} = {result}")
            print("Result:", result)

# Run the calculator
if __name__ == "__main__":
    main()