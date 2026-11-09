# Citizen Identity Management System

## About the Project

This is one of my first Python projects, which I created when I started learning Python.

The project is a simple Citizen Identity Management System. It works like a basic NADRA system where a citizen can log in using a CNIC number and view or update their information.

It uses a Python dictionary to store citizen data and a JSON file to save updated information.

## Features

- Login using CNIC number
- Show available CNIC numbers before login
- Check CNIC format
- View citizen identity profile
- Update home address
- Save updated address in a JSON file
- Check CNIC status
- Logout from the current citizen
- Exit the complete system

## Technologies Used

- Python
- Dictionaries
- While Loops
- Conditional Statements
- Functions
- JSON
- File Handling

## Project Structure

```text
Citizen-Identity-Management-System/
│
├── main.py
├── citizens.json
├── README.md
└── .gitignore
```

## How to Run

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

```bash
python main.py
```

## How It Works

First, the system shows the available CNIC numbers. The user enters a CNIC number to log in.

After successful login, a menu appears with different options:

1. View Identity Profile
2. Update Home Address
3. Check CNIC Status
4. Logout from Citizen
5. Exit System

When the address is updated, the new information is saved in a JSON file. If the user logs out, they can log in again using another citizen's CNIC.

## What I Learned

While making this project, I practiced:

- Working with dictionaries and nested dictionaries
- Using while loops and if-else conditions
- Taking input from users
- Creating and using functions
- Reading and writing JSON files
- Updating dictionary data
- Working with nested loops

## Future Improvements

- Add a PIN or password for login.
- Add an option to register new citizens.
- Add an option to delete citizen records.
- Improve input validation.

## Note

This is only a practice project made for learning Python. It is not connected to the real NADRA database and uses sample citizen information.

## Author

### Junaid Saleem

- **GitHub:** [JS-JUNAIDSALEEM](https://github.com/JS-JUNAIDSALEEM)
- **LinkedIn:** [Junaid Saleem](https://www.linkedin.com/in/junaid-saleem-developer/)