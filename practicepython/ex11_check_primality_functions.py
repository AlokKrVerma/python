def get_interger_input():

    num = input("Enter one number[Type exit to finish]: ")
    if num.lower() == 'exit':
        exit()

    while True:
        if num.lower() == 'exit':
            exit()
        try:
            num = abs(int(num))
            return num
        except:
            num = ''
        num = input("You haven't entered number correctly. Reenter one number[Type exit to finish]: ")


while True:
    num = get_interger_input()
    prime = 1
    if num in [1,2]:
        print("Its a prime number")
        continue

    for i in range(2, num-1):
        if num % i == 0:
            prime = 0

    if prime == 0:
        print("Its a not prime number")
    else:
        print("its a prime number")