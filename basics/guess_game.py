import random

print("Welcome, Let's Play Number Guessing Game :) ")
number_guess = random.randint(1,100)

attempts = 0

while True:
   
    player_guess = input("Guess The Number Between (1-100) ")
    
    if player_guess.isdigit():
        player_guess = int(player_guess)
        if player_guess == number_guess:
            print("Nice Guess, You Got it :)")
            attempts += 1
            print(f"You got it right after {attempts} attempts")
            quit()
        
        else:
            if player_guess > number_guess:
                print("Too high")
            else:
                print("Too low")
            print("Wrong :( Try Again")
            attempts +=1
        
    else:
        print("Please Enter only Numbers!")
        continue
    
