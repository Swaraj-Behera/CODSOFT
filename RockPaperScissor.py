#Made by  TRAJ
import random

def comp_Output():
    r = random.randint(1, 3) 
    if r == 1:
        return "Rock"
    elif r == 2:
        return "Paper"
    elif r == 3:
        return "Scissor"

def user_Output(user_input):
    if user_input == 1:
        return "Rock"
    elif user_input == 2:
        return "Paper"
    elif user_input == 3:
        return "Scissor"
    else:
        print("You have entered an invalid input!")
        return None

def result(user, comp):
    if user == comp:
        print("Tie")
    elif (user == "Rock" and comp == "Scissor") or \
         (user == "Paper" and comp == "Rock") or \
         (user == "Scissor" and comp == "Paper"):
        print("User Won!")
    else:
        print("Computer Won!")

while True:
    try:
        user_input = int(input("1. For Rock\n2. For Paper\n3. For Scissor\nEnter your choice: "))
        user_choice = user_Output(user_input)
        if user_choice:
            comp_choice = comp_Output()
            print(f"Computer chose: {comp_choice}")
            print(f"User chose: {user_choice}")
            result(user_choice, comp_choice)

            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again != 'yes':
                print("Thanks for playing!")
                break
    except ValueError:
        print("Please enter a valid number!")
      #Made by TRAJ
