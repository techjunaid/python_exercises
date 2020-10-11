                                         # Snake Water Gun
import random
chance =3
no_of_chance=0
computer_point=0
your_point=0

lst = ["s","w","g"]
rand_num = random.choice(lst)
# print(rand_num)
# user_input = input("enter your choice from s, w, g :: ")
#
# if rand_num==user_input:
#     print("Tie both have 0 points")

while no_of_chance<chance:
    rand_num = random.choice(lst)
    user_input = input("enter your choice from s, w, g :: ")

    if rand_num == user_input:
        print("Tie both have 0 points")


    elif rand_num == 'g'and user_input == 's':

        print(" computer wins")
        print(" bcos computer have chosen the gun")
        computer_point +=1
        chance -=1
        print("you have only ",chance," chance left")


    elif rand_num== 'g' and user_input=='w':
        print("you win")
        print(" bcos computer have chosen the gun ")
        your_point+=1
        chance -= 1
        print("you have only ", chance, " chance left")

    elif rand_num== 's' and user_input=='w':
        print("computer win")
        print(" bcos computer have chosen the snake")
        computer_point+=1
        chance -= 1
        print("you have only ", chance, " chance left")


    elif rand_num== 'w' and user_input=='g':
        print("computer win")
        print("bcos computer have chosen the water ")
        computer_point += 1
        chance -= 1
        print("you have only ", chance, " chance left")


    elif rand_num== 'w' and user_input=='s':
        print("you win")
        print(" bcos computer have chosen the water")
        your_point += 1
        chance -= 1
        print("you have only ", chance, " chance left")

    elif rand_num== 's' and user_input=='g':
        print("you win")
        print(" bcos computer have chosen the snake")
        your_point+=1
        chance -= 1
        print("you have only ", chance, " chance left")

    elif rand_num== 's' and user_input=='w':
        print("computer win")
        print(" bcos computer have chosen the snake")
        computer_point += 1
        chance -= 1
        print("you have only ", chance, " chance left")

    no_chance = no_of_chance+1


if chance==no_of_chance:
    print(" \n GAME OVER !!!!!!!!!\n ")
    print("you have earned",your_point,"points")
    print("computer have ",computer_point,"points")

# print(your_point)
# print(computer_point)

if your_point>computer_point:
    print(" \n your points is greater than computer \n  SO YOU WIN")

else:
    print("\n computer points is greater than you \n SO COMPUTER WINS")

