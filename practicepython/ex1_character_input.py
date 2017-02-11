# Ask user to enter his/her name
username = str(input("Please enter you name: "))

# Validate name
while len(username) == 0 or not isinstance(username, str):
    username = str(input(" You haven't entered your name correctly. Please enter you name: "))

# Ask user to enter his/her age
try:
    age = int(input("Please enter you age: "))
except:
    age = ''

# Validate age considering age could also be 0 years
while len(str(age)) == 0 or 0 < age > 99:
    try:
        age = int(input(" You haven't entered your age correctly. Age must be between 0 and 99 inclusive. Please enter you age: "))
    except ValueError:
        continue
# calculate current year
currentyear = datetime.date.today().year

# print message
print( " Hi {}, You will turn 100 in {}".format(username, currentyear + (100 - int(age))))