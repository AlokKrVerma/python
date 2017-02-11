# Ask user to enter his/her name
user1 = str(input("Please enter you name [User1]: "))

# Validate name
while len(user1) == 0 or not isinstance(user1, str):
    user1 = str(input(" You haven't entered your name correctly. Please enter you name [User1]: "))

# Ask user to enter his/her name
user2 = str(input("Please enter you name [User2]: "))

# Validate name
while len(user2) == 0 or not isinstance(user2, str):
    user2 = str(input(" You haven't entered your name correctly. Please enter you name [User2]: "))

user1_choice = str(input("Please enter you choice User1 [ Rock, Paper, Scissor ]: "))
while len(user1_choice) == 0 or not isinstance(user1_choice, str) or user1_choice.lower() not in ['rock' , 'paper' , 'scissor']:
    user1_choice = str(input(" You haven't entered your option correctly. Please enter you choice User1 [ Rock, Paper, Scissor ]: "))

user2_choice = str(input("Please enter you choice User2 [ Rock, Paper, Scissor ]: "))
while len(user2_choice) == 0 or not isinstance(user2_choice, str) or user2_choice.lower() not in ['rock' , 'paper' , 'scissor']:
    user1_choice = str(input(" You haven't entered your option correctly. Please enter you choice User2 [ Rock, Paper, Scissor ]: "))

if user1_choice.lower() == 'rock':
    if user2_choice.lower() == 'paper':
        print(" {} wins".format(user2))
    elif user2_choice.lower() == 'scissor':
        print(" {} wins".format(user1))
    else:
        print("Its a tie")
elif user1_choice.lower() == 'paper':
    if user2_choice.lower() == 'rock':
        print(" {} wins".format(user1))
    elif user2_choice.lower() == 'scissor':
        print(" {} wins".format(user2))
    else:
        print("Its a tie")
elif user1_choice.lower() == 'scissor':
    if user2_choice.lower() == 'rock':
        print(" {} wins".format(user2))
    elif user2_choice.lower() == 'paper':
        print(" {} wins".format(user1))
    else:
        print("Its a tie")
else:
    print("wrong options. PLease check. User1: {}, User2: {} , User1_Choice: {}, User2_Choice: {}".format(user1, user2, user1_choice, user2_choice))