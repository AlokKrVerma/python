# Ask user to enter his/her name
username = str(input("Please enter you name: "))

# Validate name
while len(username) == 0 or not isinstance(username, str):
    username = str(input(" You haven't entered your name correctly. Please enter you name: "))

if username == username[-1::-1]:
    print("Your name is palindrome")
else:
    print("Your name is not a palindrome")

