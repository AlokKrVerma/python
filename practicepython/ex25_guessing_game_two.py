import math


def guess(last_guessed, tries, resp):
    if resp.lower() == "too high":
        num = range(1,50)
    else:
        num = range(51,101)

    while True:
        tries += 1
        last_guessed = num[math.floor(len(num) / 2)]
        resp = input("Is it {}? (Yes/too high/too low)".format(last_guessed))
        if resp.lower() == "yes":
            print("I guessed it in {} tries".format(tries))
            return
        elif resp.lower() == "too high":
            num = num[: math.floor(len(num) / 2)]
        else:
            num = num[math.floor(len(num) / 2):]


def main():
    input("Guess a number between 1 and 100. Press enter when you are ready: ")
    tries = 1
    last_guessed = 50
    resp = input("Is it 50? (Yes/too high/too low)")
    if resp.lower() == "yes":
        print("I guessed it in {} tries".format(tries))
    else:
        guess(last_guessed, tries, resp)

if __name__ == "__main__":
    main()
