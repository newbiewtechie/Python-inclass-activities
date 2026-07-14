import random

while True:
    user_action = input("Enter your choice")
    possible_actions = ["rock", "paper", "scissors"]
    robot = random.choice(possible_actions)
    print(f"\nYou chose {user_action},  and robot chose {robot}\n")
    if user_action== robot:
        print("Its a draw")
    elif user_action =="rock":
        if robot == "paper":
            print("robot has won ")
        else:
            print("You have won ")
    elif user_action == "paper":
        if robot == "scissors":
            print("robot has won ")
        else :
            print("you have won ")
    elif user_action == "scissors":
        if robot == "rock":
            print("robot has won")
        else:
            print("you have won")
    play_again =  input ("Play again (yes/no): ")
    if play_again == "yes":
        break
