import json
import os

path = "data/phonebook.json"

if not os.path.exists("data"):
    os.makedirs("data")
if not os.path.exists(path):
    with open(path, "w", encoding="utf-8") as file:
        json.dump([], file)


def read_file_contacts() -> list:
    try:
        if not os.path.exists(path):
            return []
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("JSON database is corrupted. So, a new one is created.")
        return []
    except Exception as e:
        print(f"Exception occured: {e}. So, a new one is created.")
        return []


def save_contacts(data: list):
    try:
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Exception occured while saving contacts: {e}.")


phone_book = read_file_contacts()
running = True

while running:
    msg = """
    A. Add Contact
    G. Get Contact
    E. Exit
"""
    try:
        c = input(msg).upper()

        if c in ["A", "ADD", "A. ADD CONTACT", "ADD CONTACT"]:
            u = input("enter user: ").strip()

            if any(contact["name"].lower() == u.lower() for contact in phone_book):
                print(f"Error: User '{u}' already exists!")
                continue

            work = input("enter work: ").strip()
            email = input("enter email: ").strip()
            mobile = input("enter mobile: ").strip()

            if not u or not mobile:
                print("Error: Name and Mobile cannot be empty!")
                continue

            phone_book.append(
                {"name": u, "work": work, "email": email, "mobile": mobile}
            )

            save_contacts(phone_book)
            print(f"Contact '{u}' added successfully.")

        elif c in ["G", "GET", "G. GET PHONE", "GET PHONE", "GET CONTACT"]:
            u = input("Enter user name to search: ").strip().lower()

            contact = next(
                (c for c in phone_book if c["name"].lower() == u.lower()), None
            )

            if contact:
                print(f"Contact found: {contact}")
            else:
                print(f"Contact '{u}' not found.")
        elif c in ["E", "EXIT", "E. EXIT"]:
            print("Exiting phonebook. Goodbye!")
            running = False

        else:
            print("Invalid option. Please enter valid choices like A, G, or E.")

    except Exception as e:
        print(f"An unexpected error happened: {e}")
