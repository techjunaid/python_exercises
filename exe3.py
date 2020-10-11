n=18
att=9
print("you have only 5 attempts ")
for i in range(9):
    item = int(input("Guess the number :: \n"))

    if item==n:
        print("you won and you had",att-1,"attempts left")
        break
    elif item<n and att !=1:
        print("you should enter a larger number ",)
        print("you have", att-1 ," attempt left ")
        att-=1
    elif item>n and att !=1:
        print("you should enter a lesser number ")
        print("you have", att-1 , " attempt left ")
        att -= 1
    elif (item<9 or item>9) and att==1:
        print("Game Over\n you have 0 attempts left \n better luck for next time !")

    i+=1