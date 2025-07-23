import time
import random

print("This is Guess The Number")
time.sleep(1.5)
print("The computer will randomly select a number between 1 and 100")
time.sleep(1.5)
print("You have to guess it, and you will get hints along they way")
time.sleep(1.5)
print("Good luck!\n")
time.sleep(2)

j = open("highscore.txt", "r")
istherecontent = j.read()
j.close()

k = open("highscore.txt", "w")
if (istherecontent==""):
    k.write("100")
k.close()



global i
i=0

def play():
    selected_number = random.randint(1, 100)
    found = False
    tries=0
    
    while found==False:
        guess = int(input("Enter guess: "))
        if (guess<selected_number):
            print("Higher\n")
            tries +=1
        elif (guess>selected_number):
            print("Lower\n")
            tries +=1
        else:
            found = True
            print("\nCorrect!")
            print(f"You took {tries} tries")
            a = open("highscore.txt", "r")
            current_score = a.read()
            a.close()
            if (tries<int(current_score)):
                print("New High Score!")
                b = open("highscore.txt", "w")
                b.write(str(tries))
                b.close()
            global i
            i+=1
            c = open("score_history.txt", "a")
            c.write(f"Game {i}: {tries} tries\n")
            c.close()
    
    print("Do you want to view game history?")
    historycheck = input("1 for yes 2 for no: ")
    if historycheck=="1":
        h = open("score_history.txt", "r")
        history_to_check = h.read()
        h.close()
        time.sleep(1)
        print(f"\n{history_to_check}\n")

    print("Play again? 1 for yes 2 for no: ")
    print("(High score and score history clears if you enter 2)")
    playagain = input("")
    print("\n")
    if playagain=="1":
        play()
    if playagain=="2":
        f = open("score_history.txt", "w")
        f.write("")
        f.close()

        g = open("highscore.txt", "w")
        g.write("")
        g.close

play()