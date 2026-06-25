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
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
    with open(path, "a", encoding="utf-8") as file:
        file.write(f"{user} -- {phone}\n")


# ---


phone_book = read_file_contacts()
running = True

while running:
    msg = """
    1. add contact
    2. get phone
    3. exit
"""
    try:
        c = input(msg)
        if c == "1":
            u = input("enter user: ")
            # TODO: check if the user already exists in the dictionary
            phone = input("enter phone: ")
            # TODO: assert that user name and phone dose not have "--" in them

            phone_book[u] = phone
            add_contact_to_file(u, phone)
        elif c == "2":
            u = input("enter user: ")
            print(u, "phone:", phone_book[u])

        elif c == "3":
            running = False
        else:
            print("enter a valid number:")
    except:
        print("some error happened !!!")
