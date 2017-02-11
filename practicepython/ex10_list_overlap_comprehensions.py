import random
a = random.sample(range(1,100), 10)
b = random.sample(range(1,50), 20)

# new_list = [ num1 for num1 in set(a) for num2 in set(b) if num1 == num2]
print("First list: {}".format(sorted(a)) )
print("Second list: {}".format(sorted(b)) )
new_list = [ num for num in set(a) if num in b]

print("Final list: {}".format(new_list))
