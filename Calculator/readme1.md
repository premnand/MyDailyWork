# Simple Calculator

## Overview

This is a simple command-line calculator implemented in Python. It evaluates arithmetic expressions and keeps a history of calculations. The calculator supports basic arithmetic operations and provides feedback on invalid inputs.

## Features

- Basic Arithmetic Operations: Addition, subtraction, multiplication, and division.
- alculation History: Stores and displays previous calculations.
- Error Handling: Provides informative error messages for invalid inputs and operations.
- Exit Command: Type exit to quit the application.
- History Command: Type history to view past calculations.

## Requirements

- Python 3.x
  
## Usage

1. Run the Calculator:

    - Execute the script using Python:
```
python calculator.py
```

2. Enter Calculations:

    - Input arithmetic expressions like 2+2, 5*3, etc., and press Enter to see the result.

3. View History:

    - Type history to display a list of previous calculations and their results.

4. Exit the Program:

    - Type exit to close the calculator.
    - 
### Example

```
Simple Calculator
Type 'exit' to quit
Type 'history' to view past calculations
Enter a calculation (e.g., 2+2): 3+5
Result: 8
Enter a calculation (e.g., 2+2): 10/2
Result: 5.0
Enter a calculation (e.g., 2+2): history
Calculation History:
3+5 = 8
10/2 = 5.0
Enter a calculation (e.g., 2+2): exit
Exiting the calculator.
```

## Error Handling

- Invalid Syntax: If an invalid syntax is entered, an error message will be shown.
- Invalid Characters: Input containing invalid characters or variables will result in an error.
- Division by Zero: Dividing by zero will return an appropriate error message.
  
## Security Note

This calculator uses eval() to evaluate expressions. While it's suitable for this simple example, be cautious with eval() in production environments, as it can execute arbitrary code. For safer evaluation, consider using libraries designed for expression parsing.

## License
This project is licensed under the MIT License. See the LICENSE file for details.