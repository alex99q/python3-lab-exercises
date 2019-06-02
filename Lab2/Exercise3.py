import random

secret_num = random.randrange(1, 11, 1)
player_num = int(input("Guess a number from 1 to 10: "))

list_of_player_nums = [player_num]

while player_num != secret_num:
    if player_num > secret_num:
        print("Too high!")
    elif player_num < secret_num:
        print("Too low!")

    player_num = int(input("Guess again: "))

    if player_num not in list_of_player_nums:
        list_of_player_nums.append(player_num)

print("You won with " + str(len(list_of_player_nums)) + " tries!")