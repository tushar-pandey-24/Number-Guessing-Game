import random

logo = """
  ________                                __  .__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ _/  |_|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/ \   __\  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \   |  | |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >  |__| |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/             \/     \/          \/            \/    \/     \/       
"""

print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

level = input("Choose a difficulty level. Type 'easy' or 'hard'.\n").lower()

number = random.randint(1, 100)

def play_game():
    player_lives = 10
    if level == "hard":
        player_lives = 5
    game_over = False
    while not game_over:
        print(f"You have {player_lives} attempts remainig to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number:
            game_over = True
            print(f"The number was {number}. You won!")
        else:
            player_lives -= 1
            if player_lives == 0:
                game_over = True
                print("You ran out of lives. Game Over!")
            elif guess > number:
                print("Too High\nGuess again.")
            elif guess < number:
                print("Too Low.\nGuess again.")
    

play_game(level)
