import random
playing = True
number = str(random.randint(10, 20))
print("I will generate a number between 0, 9 and you have to guess the number")
print("The game end when you get 1 hero")
while playing:
    guess = input("Give a number ")
    if number == guess:
        print("You won the game.")
        print("The numer was ", number)
        break
    else:
        print("Youe guess is not correct. Try again.")