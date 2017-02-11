# Ask user to enter a number
try:
    num = int(input("Please enter a number: "))
except:
    num = ''

while len(str(num)) == 0 :
    try:
        num = int(input(" You haven't entered number correctly. Please enter a number again "))
    except ValueError:
        continue

# initiate empty list to hold divisors
divisor = []

# use abs to handle negative numbers
for i in range(1, abs(num)+1):
    if num % i == 0:
        divisor.append(i)

print(divisor)