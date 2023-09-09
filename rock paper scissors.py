import random
def get_user_choice():
    while True:
        user_choice= input("Enter your choice (rock/paper/scissors): ").lower()
        if user_choice in ["rock","paper","scissors"]:
            return user_choice
        else:
            print("Invalid choice.Please chosoe rock,paper,or scissors.")
#computer choosing the random choice
def get_computer_choice():
    choices =["rock","paper","scissors"]
    return random.choice(choices)
#determining winner comparing both the choices of user and the computer

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "its a tie!!"
    elif (
        (user_choice =="rock" and computer_choice =="scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice =="scissors" and computer_choice == "paper")
    ):
            
        return "you win!!"
    else:
        return "computer wins!!"

def main():
    print("welcome to Rock-paper_scissors.!!")
    user_choice = get_user_choice()
    computer_choice=get_computer_choice()
    print(f"your choice: {user_choice}")
    print(f"computer's choice:{computer_choice}")
    result=determine_winner(user_choice,computer_choice)
    print(result)

if __name__=="__main__":
    main()

    

