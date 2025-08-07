

import random


attempts_list = []


def show_score():
    if len(attempts_list) <= 0:
        print("Hey! You don't have any current high scores. Try and achieve them!")
    else:
        print("Your current high score is", min(attempts_list))


def start_game():
    random_no = random.randint(1, 10)
    print("Hey there! Welcome to the game of Guessing!")
    name = input("Enter your name: ")
   
    print("Hi", name + "! Would you like to play the game?")
    want_play = input("ENTER (Yes/No): ").lower()


    attempts = 0
    show_score()


    while want_play == "yes":
        try:
            guess = int(input("Enter a number between 1 to 10: "))
            if guess < 1 or guess > 10:
                raise ValueError("Please enter a number between 1 and 10.")


            attempts += 1


            if guess == random_no:
                print("Congrats! You have guessed the correct number!")
                print("It took you", attempts, "attempt(s).")
                attempts_list.append(attempts)
                show_score()


                play_again = input("Do you want to play again? (Yes/No): ").strip().lower()
                if play_again == "no":
                    print("That's cool! Have a nice day!")
                    break
                else:
                    attempts = 0
                    random_no = random.randint(1, 10)


            elif guess < random_no:
                print("It's higher.")


            elif guess > random_no:
                print("It's lower.")


        except ValueError as err:
            print("Oh! That's not a valid number. Please try again!")
            print("({})".format(err))


if __name__ == '__main__':  
    start_game()



