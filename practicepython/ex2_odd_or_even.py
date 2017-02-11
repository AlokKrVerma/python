try:
    num = int(input("Please an integer: "))
except:
    num = ''

# Validate age considering age could also be 0 years
while len(str(num)) == 0 :
    try:
        num = int(input(" You haven't entered number correctly. Please enter again: "))
    except ValueError:
        continue

if num % 4 == 0:
    print("This is an even number which is dividable by 4")
elif num % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")