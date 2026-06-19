

# from pathlib import Path


path = "data/phonebook.txt"

with open(path,"r") as file:
    raw_file = file.read()

for line in raw_file.split("\n"):
    u, phone = line.split("--")
    u = u.strip()
    phone = phone.strip()



