
# y = int(input("y="))

y = 2000
while y < 3000:
    print(y,end=" ")
    if y % 400 == 0:
        print("yes")
    elif y % 100 == 0:
        print("no")
    elif y % 4 == 0:
        print("yes")
    else:
        print("no") 
    y = y + 1  

