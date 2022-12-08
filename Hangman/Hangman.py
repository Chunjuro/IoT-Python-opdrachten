import random
from collections import Counter
with open ("./woordlijst.txt", "r") as woordlijst:
    woorden = woordlijst.readlines()

woord = (random.choice(woorden)).strip()
lengte_woord = len(woord)
lives = 0
juist = []
fout = []
geraden = 0
kansen = 6

hangman = "  ___"
hangman1 = " /  |"
hangman2 = " |"
hangman3 = " |"
hangman4 = " |"
hangman5 = "_|_"

while True:
    print("juiste letters", juist)
    print("foute letters", fout)
    print("je hebt nog zoveel kansen over:", kansen)

    print(hangman)
    print(hangman1)
    print(hangman2)
    print(hangman3)
    print(hangman4)
    print(hangman5)

    for l in woord:
        if l in juist:
            print(l, end="")
        else:
            print("_", end="")

    if lives == 6:
        print("\nyou are dead")
        print("het woord was", woord)
        exit()
    if geraden == lengte_woord:
        exit("\nproficiat, je hebt het woord geraden")

    gok = input("\ngeef een letter: ")
    if gok in juist:
        print("jij hebt deze letter al gebruikt")
    elif gok in fout:
        print("jij hebt deze letter al gebruikt")
    elif gok in woord:
        juist.append(gok)
        geraden += 1
        continue
    elif gok not in woord:
        print("fout")
        fout.append(gok)
        lives += 1
        if lives == 1:
            hangman2 = " |  O"
        elif lives == 2:
            hangman3 = " |  |"
        elif lives == 3:
            hangman3 = " | /|"
        elif lives == 4:
            hangman3 = " | /|\\"
        elif lives == 5:
            hangman4 = " | /"
        else:
            hangman4 = " | / \\"
        kansen -= 1
        continue
    
    