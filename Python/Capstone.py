import random
attempts_list=[]
def showscore():
    if len(attempts_list)<=0:
        print("Hey! You don't have any current high scores. Try and Achieve them")
    else:
        print("Your current High score is ",min(attempts_list))

def start_game():
    random_no=int(random.randint(1,10))
    print("Hey there! Welcome to the game of Guessing")
    name=input("Enter your Name")
    want_play=print("Hi ",name,"would you like to play the game? ENTER (Yes/No)")

    attempts=0
    showscore()
    while want_play.lower()=="yes":
        try:
             guess=int(input("Enter a Number between 0 to 10"))
             if guess<0 or guess>10:
                 raise ValueError("Please enter a Number between 0 and 10")
             if guess==random_no:
                 print("Congrats! You have guessed the correct Number")
                 attempts+=1
                 attempts_list.append(attempts)
                 print("It took you ",attempts_list," attempts")
                 play_again=input("Do you want to play again? ENTER (Yes/No)")
                 attempts=0
                 showscore()
                 random_no=int(random.randint(1,10))
                 if play_again.lower()=="no":
                     print("That's cool! Have a nice day!")
                     break
             elif guess < random_no:
                     print("It's higher")
                     attempts+=1
             elif guess > random_no:
                     print("It's lower")
                     attempts+=1
        except ValueError as err:
            print("Oh! That's not a Vlid no. Pls Try Again!")
            print("({})".format(err))
if __name__=='_main_':
    start_game()