import random

my_number = random.randint(1,9)
guessed = 0
wins = 0

while True:
    num = input("Please enter one number [Type exit to finish]: ")
    if num.lower() == 'exit':
        print("You played {} times and winned {} times".format(guessed, wins))
        exit()

    my_number = random.randint(1, 9)
    guessed = guessed + 1
    try:
        num = int(num)
    except:
        print("You haven't entered a valid number.")
        continue

    if my_number == num:
        print(" Congratulations. You guess is correct")
        wins = wins +1
    elif my_number < num and abs(num - my_number) > 5:
        print("You guess too high")
    elif my_number > num and abs(num - my_number) > 5:
        print("You guess too low")

    print("You guessed {} and number was {}".format(num, my_number))