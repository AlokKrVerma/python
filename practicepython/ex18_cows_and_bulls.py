import random
import string

total_cows = 0
total_bulls = 0

def get_interger_input():

    num = input("Enter four digit positive number[Type exit to finish]: ")
    if num.lower() == 'exit':
        print(" Thanks for playing. You got total {} cows and {} bulls in this game".format(total_cows, total_bulls))
        exit()

    while True:
        if num.lower() == 'exit':
            print(
                " Thanks for playing. You got total {} cows and {} bulls in this game".format(total_cows, total_bulls))

            exit()
        try:
            num = int(num)
            if len(str(num)) == 4:
                return num
        except:
            num = ''

        num = input("You haven't entered number correctly. Reenter four digit positive number[Type exit to finish]: ")


while True:
    user_number = str(get_interger_input())
    internal_num = ''.join((random.choice(string.digits) for i in range(4)))
    game_specific_cows = 0
    game_specific_bulls = 0

    for i in range(4):
        if user_number[i] == internal_num[i]:
            game_specific_cows += 1
        else:
            game_specific_bulls += 1

    print(" You got {} cows and {} bulls in this specific game".format(game_specific_cows, game_specific_bulls))
    total_bulls += game_specific_bulls
    total_cows += game_specific_cows

    continue



