# Citizen Identity Management System

import json
import os

# Simulated NADRA Database (CNIC numbers as keys)
citizens = {
    "35201-1234567-1": {
        "name": "Ali Khan",
        "father_name": "Ahmed Khan",
        "dob": "15-08-1995",
        "address": "House 12, Street 3, Lahore",
        "status": "Active",
        "pin": "1234"
    },
    "42101-9876543-2": {
        "name": "Ayesha Ahmed",
        "father_name": "Ahmed Bilal",
        "dob": "22-11-2001",
        "address": "Sector F-11, Islamabad",
        "status": "Active",
        "pin": "2345"
    },
    "33100-4567891-3": {
        "name": "Usman Malik",
        "father_name": "Tariq Malik",
        "dob": "10-03-1998",
        "address": "Model Town, Lahore",
        "status": "Active",
        "pin": "3456"
    },
    "61101-2345678-4": {
        "name": "Fatima Noor",
        "father_name": "Khalid Noor",
        "dob": "25-06-2000",
        "address": "G-10, Islamabad",
        "status": "Active",
        "pin": "4567"
    },
    "37405-7654321-5": {
        "name": "Hassan Raza",
        "father_name": "Rashid Raza",
        "dob": "18-12-1997",
        "address": "Satellite Town, Rawalpindi",
        "status": "Active",
        "pin": "5678"
    },
    "71101-3456789-6": {
        "name": "Sara Ahmed",
        "father_name": "Imran Ahmed",
        "dob": "05-04-2002",
        "address": "University Road, Peshawar",
        "status": "Active",
        "pin": "6789"
    },
    "17301-8765432-7": {
        "name": "Bilal Hussain",
        "father_name": "Nadeem Hussain",
        "dob": "30-09-1996",
        "address": "Cantt Area, Quetta",
        "status": "Inactive",
        "pin": "7890"
    },
    "45202-5678912-8": {
        "name": "Zainab Ali",
        "father_name": "Javed Ali",
        "dob": "12-01-2003",
        "address": "Civil Lines, Faisalabad",
        "status": "Active",
        "pin": "8901"
    }
}

# Check CNIC format

def check_cnic(cnic):
    if len(cnic) == 15:
        if cnic[5] == "-" and cnic[13] == "-":
            if cnic[:5].isdigit() and cnic[6:13].isdigit() and cnic[14].isdigit():
                return True
    return False

# Validate citizen data

def validate_citizens(data):
    if not isinstance(data, dict) or not data:
        return False

    required_fields = ["name", "father_name", "dob", "address", "status", "pin"]

    for cnic, user_data in data.items():
        if not check_cnic(cnic):
            return False

        if not isinstance(user_data, dict):
            return False

        for field in required_fields:
            if field not in user_data or not isinstance(user_data[field], str):
                return False

        if len(user_data["pin"]) != 4 or not user_data["pin"].isdigit():
            return False

    return True

# Load citizen data from JSON file

def load_citizens():
    if os.path.exists("citizens.json"):
        try:
            with open("citizens.json", "r") as file:
                saved_citizens = json.load(file)

                if validate_citizens(saved_citizens):
                    return saved_citizens

                print("Saved data has an invalid structure. Starting with sample data.")

        except (json.JSONDecodeError, OSError):
            print("Could not load saved data. Starting with sample data.")

    return citizens

# Save citizen data in JSON file

def save_citizens(citizens):
    with open("citizens.json", "w") as file:
        json.dump(citizens, file, indent=4)


# Main System Function

def main():

# Load saved data
    citizens = load_citizens()

    print("\n====== WELCOME TO CITIZEN IDENTITY SYSTEM ======\n")

    system_running = True

# Main System Loop
    while system_running:

        # 1. Login System using CNIC

        while True:
            enter_cnic = input("Enter your CNIC (e.g., 35201-1234567-1): ").strip()

            if not check_cnic(enter_cnic):
                print("Invalid CNIC format. Please try again.\n")
                continue

            if enter_cnic in citizens:

                enter_pin = input("Enter your 4-digit PIN: ").strip()

                if enter_pin == citizens[enter_cnic]["pin"]:
                    print(f"\nVerification successful. Welcome, {citizens[enter_cnic]['name']}!")

                    # Store the current logged-in citizen's data for easy access
                    user_data = citizens[enter_cnic]
                    break

                else:
                    print("Incorrect PIN. Please try again.\n")

            else:
                print("CNIC not found in database. Please try again.\n")

        # 2. Main Menu Loop

        while True:
            print("""
=========== Citizen Identity Menu ==========
1. View Identity Profile
2. Update Home Address
3. Check CNIC Status
4. Logout from Citizen
5. Exit System
""")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":

                # Display all profile details
                print("\n--- Identity Profile ---")
                print(f"Full Name:     {user_data['name']}")
                print(f"Father's Name: {user_data['father_name']}")
                print(f"Date of Birth: {user_data['dob']}")
                print(f"Address:       {user_data['address']}")

            elif choice == "2":

                # Update the address
                new_address = input("Enter your new home address: ").strip()

                if new_address == "":
                    print("Address cannot be empty.")

                else:
                    user_data['address'] = new_address
                    save_citizens(citizens)
                    print("Address updated successfully!")

            elif choice == "3":

                # Check card validity status
                print(f"Your CNIC status is currently: {user_data['status']}")

            elif choice == "4":
                print("You have successfully logged out.\n")
                break

            elif choice == "5":
                print("Thank you for using the system. Goodbye!")
                system_running = False
                break

            else:
                print("Invalid choice. Select an option from 1 to 5.")


# Run the system only when this file is executed directly

if __name__ == "__main__":
    main()
