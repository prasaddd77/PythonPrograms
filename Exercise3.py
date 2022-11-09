n=32
i=1
while i <= 9:
    a = int(input("Guess the number: "))
    if a > 32:
        print("Too high!")
    elif a < 32:
        print("Too low!")
    else:
        print("You won\n")
        print(i,"are the number of guesses you took.\n")
        break
    print(9-i,"are the number of guesses left.")
    i=i+1
    if i>9:
        print("GAME OVER!!!")