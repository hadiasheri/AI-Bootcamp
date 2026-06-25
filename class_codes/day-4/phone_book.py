
path = "data/phonebook.txt"

def read_file_contacts():
    with open(path,"r") as file:
        raw_file = file.read().strip()

    file_phones = {}
    for line in raw_file.split("\n"):
        u, phone = line.split("--")
        u = u.strip()
        phone = phone.strip()
        file_phones[u] = phone
    
    return file_phones

def add_contact_to_file(user,phone):
    with open(path,"a") as file:
        file.write(user)
        file.write(" -- ")
        file.write(phone)
        file.write("\n")


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
            add_contact_to_file(u,phone)
        elif c == "2":
            u = input("enter user: ")
            print(u ,"phone:", phone_book[u])

        elif c == "3":
            running = False
        else:
            print("enter a valid number:")
    except:
        print("some error happened !!!")