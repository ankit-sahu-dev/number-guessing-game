import random

secret_number = random.randint(1,100) 
guess = 0
attempts = 0
print("||...WELCOME TO THE GUESS NUMBER GAME...||")

attempts += 1

while guess != secret_number:
    guess = int(input("Guess the number: "))
    attempts += 1
    
    if guess > secret_number:
        print("Too high!!")
    elif guess < secret_number:
        print("Too low!!")
    else:
        print("Correct, You won!")
print("Total attempts:", attempts)