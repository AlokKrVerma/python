prime_list = []
happy_list = []

with open("E23_Prime_Number.txt", 'r') as prime_file_read:
    for prime in prime_file_read.readlines():
        prime_list.append(int(prime.replace("\n", '')))

with open("E23_Happy_Number.txt", 'r') as happy_file_read:
        for happy in happy_file_read.readlines():
            happy_list.append(int(happy.replace("\n", '')))

print([ prime for prime in prime_list if prime in happy_list ])