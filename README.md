# Citizen Identity Management System

## About the Project

This is one of my first Python projects, which I created when I started learning Python.

The project is a simple Citizen Identity Management System. It works like a basic NADRA system where a citizen can log in using a CNIC number and a 4-digit PIN to view or update their information.

It uses a Python dictionary to store citizen data and a JSON file to save updated information.

## Features

- Login using CNIC number and PIN
- Check CNIC format
- Verify citizen PIN before login
- View citizen identity profile
- Update home address
- Remove extra spaces from the updated address
- Save updated information in a JSON file
- Check CNIC status
- Validate citizen data loaded from JSON
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
- unittest

## Project Structure

```text
Citizen-Identity-Management-System/
│
├── main.py
├── README.md
├── .gitignore
│
├── tests/
│   └── test_main.py
│
└── output/
    └── Identity_Menu.png
```

**Note:** `citizens.json` is created locally when a citizen's address is updated. It is excluded from GitHub through `.gitignore`, so it is not included in the repository.

## How to Run the Project

**1. Clone the repository**

```bash
git clone https://github.com/JS-JUNAIDSALEEM/Citizen-Identity-Management-System.git
```

**2. Open the project folder**

```bash
cd Citizen-Identity-Management-System
```

**3. Run the application**

```bash
python main.py
```

## How It Works

First, the user enters their CNIC number. The system checks the CNIC format and verifies whether the CNIC exists in the database.

After entering the correct CNIC, the user must enter a 4-digit PIN to log in.

After successful login, a menu appears with different options:

1. View Identity Profile
2. Update Home Address
3. Check CNIC Status
4. Logout from Citizen
5. Exit System

When the address is updated, the system removes unnecessary spaces and saves the new information in a JSON file.

If the user logs out, they can log in again using another citizen's CNIC and PIN.

The system also checks the structure of saved JSON data before loading it.

## How to Run Tests

This project uses Python's built-in `unittest` module to test important functions.

**Run the tests using this command:**

```bash
py -m unittest tests/test_main.py -v
```

The tests check:

- Valid and invalid CNIC formats
- Valid citizen data
- Missing citizen information
- Invalid PIN format
- Saving and loading citizen data
- Handling invalid JSON files

No external testing library is required.

## Demo Login

You can use the following sample account to test the system:

- **CNIC:** `35201-1234567-1`
- **PIN:** `1234`

Other sample citizen records and PINs are available in `main.py`.

## What I Learned

While making this project, I practiced:

- Working with dictionaries and nested dictionaries
- Using while loops and if-else conditions
- Taking input from users
- Creating and using functions
- Reading and writing JSON files
- Updating dictionary data
- Validating user input and citizen data
- Writing simple automated tests
- Using the main function and main guard

## Future Improvements

- Add an option to register new citizens.
- Add an option to delete citizen records.
- Improve PIN security.
- Improve input validation.

## Note

This is only a practice project made for learning Python. It is not connected to the real NADRA database and uses sample citizen information.

The PINs are stored as plain text for practice purposes. This system is not suitable for storing real citizen information.

## Author

### Junaid Saleem

- **GitHub:** [JS-JUNAIDSALEEM](https://github.com/JS-JUNAIDSALEEM)
- **LinkedIn:** [Junaid Saleem](https://www.linkedin.com/in/junaid-saleem-developer/)
