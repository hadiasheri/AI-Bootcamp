import os

path = "data/phonebook.txt"


def read_file_contacts():
    if not os.path.exists(path):
        return {}
    with open(path, "r") as file:
        raw_file = file.read().strip()

    if not raw_file:
        return {}

    file_phones = {}
    for line in raw_file.split("\n"):
        if "--" not in line:
            continue

        u, phone = line.split("--")
        u = u.strip()
        phone = phone.strip()
        file_phones[u] = phone

    return file_phones


def add_contact_to_file(user, phone):
    user = user.strip().lower()
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
    with open(path, "a", encoding="utf-8") as file:
        file.write(f"{user} -- {phone}\n")


# ---


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
            add_contact_to_file(u, phone)
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
