


import random


program_select = random.choice(["Rock","Paper","Scissor"])


msg = """ Enter a number
1) Rock
2) Paper
3) Scissor
: """

user_input = int(input(msg))

print("program choice:",program_select)


if user_input == 1 :
    # Rock
    if program_select == "Rock":
        print(" Draw ! ")
    elif program_select == "Paper" :
        print(" you lose ! ")
    elif program_select == "Scissor" :
        print(" you won ! ")
elif user_input == 2 :
    # paper
    if program_select == "Rock":
        print(" you won ! ")
    elif program_select == "Paper" :
        print(" Draw ! ")
    elif program_select == "Scissor" :
        print(" you lose ! ")
elif user_input == 3 :
    # scissor
    if program_select == "Rock":
        print(" you lose ! ")
    elif program_select == "Paper" :
        print(" you won ! ")
    elif program_select == "Scissor" :
        print(" Draw ! ")
else:
    print("please enter a number! ")
