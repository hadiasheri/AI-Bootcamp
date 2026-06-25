import json
import os

path = "data/phonebook.json"

if not os.path.exists("data"):
    os.makedirs("data")
if not os.path.exists(path):
    with open(path, "w", encoding="utf-8") as file:
        json.dump({}, file)


def read_file_contacts() -> dict[str, str]:
    try:
        if not os.path.exists(path):
            return {}
        with open(path, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("JSON database is corrupted. So, a new one is created.")
        return {}
    except Exception as e:
        print(f"Exception occured: {e}. So, a new one is created.")
        return {}


def save_contacts(data: dict[str, str]):
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
    G. Get Phone
    E. Exit
"""
    try:
        c = input(msg).upper()
        if c in ["A", "ADD", "A. ADD CONTACT", "ADD CONTACT"]:
            u = input("enter user: ").strip()

            if u in phone_book:
                print(f"Error: User '{u}' already exists!")
                continue

            phone = input("enter phone: ").strip()

            if "--" in u or "--" in phone:
                print("Error: You cannot use '--' in username or phone number!")
                continue

            if not u or not phone:
                print("Error: Name and Phone cannot be empty!")
                continue

            phone_book[u] = phone
            save_contacts(phone_book)
            print(f"Contact '{u}' added successfully.")

        elif c in ["G", "GET", "G. GET PHONE", "GET PHONE"]:
            u = input("Enter user name to search: ").strip()
            if u.lower() in phone_book:
                print(f"Contact '{u}' -> Phone: {phone_book[u]}")
            else:
                print(f"Contact '{u}' not found.")

        elif c in ["E", "EXIT", "E. EXIT"]:
            print("Exiting phonebook. Goodbye!")
            running = False
        else:
            print("Invalid option. Please enter valid choices like A, G, or E.")
    except Exception as e:
        print(f"An unexpected error happened: {e}")
