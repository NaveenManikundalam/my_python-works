import random

def play():
     rps = ["r", "p", "s"]
     comp_choice = random.choice(rps)
     comp, user = "", ""
     user_choice = input('Enter your choice "r" for rock, "s" for scissors, "p" for paper = ')

     if comp_choice == "r":comp = "Rock"
     elif comp_choice == "s": comp = "Scissors"
     else: comp = "Paper" 
     if user_choice == "r":user = "Rock"
     elif user_choice == "s": user = "Scissors"
     else: user = "Paper" 
     print(f"You chose : {user}")
     print(f"Computer chose : {comp}") 

     if (user_choice == "r" and comp_choice == "s")\
          or (user_choice == "s" and comp_choice == "p")\
          or (user_choice == "p" and comp_choice == "r"):
          print("Yes!!! You won !!!")

     elif user_choice == comp_choice:
          print("It is a Tie!!!")

     else:
          print("You lost!!!")

play()


