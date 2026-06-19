
import random

program_choice = random.choice(["Rock","Paper","Scissor"])

msg = """1) Rock
2) Paper
3) Scissor
: """

user_inp = input(msg)

if program_choice == "Rock":