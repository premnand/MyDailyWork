# Password Generator

## Overview

The Password Generator is a simple Python application that generates strong and random passwords based on user-defined length. This tool ensures that the generated passwords are complex and secure by using a combination of letters, digits, and special characters.

## Features

- **User Input**: Prompt the user to specify the desired length of the password.
- **Random Password Generation**: Generates a password using a mix of uppercase letters, lowercase letters, digits, and punctuation.
- **Display Password**: Prints the generated password on the screen.

## Requirements

- Python 3.x

## Usage

1. **Run the Application**:
   - Execute the script using Python:
     ```bash
     python password_generator.py
     ```

2. **Specify Password Length**:
   - After running the script, you'll be prompted to enter the desired length of the password.
   - The application will only accept positive integers.

3. **View Generated Password**:
   - Once the length is provided, the application will generate and display a strong, random password.

## Example

```
Password Generator
Enter the desired length of the password: 12
Generated Password: 9dZ*Fk!a2qV@
```


## Error Handling

- **Invalid Input**: If the input is not a positive integer, the application will prompt the user to try again.

## Security Considerations

- The password generator uses Python's `random` module, which is suitable for most purposes. However, for cryptographic purposes, consider using `secrets` module instead of `random`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
