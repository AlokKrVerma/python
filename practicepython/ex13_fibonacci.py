def get_interger_input():

    num = input("Enter one number[Type exit to finish]: ")
    if num.lower() == 'exit':
        exit()

    while True:
        if num.lower() == 'exit':
            exit()
        try:
            num = int(num)
            return num
        except:
            num = ''
        num = input("You haven't entered number correctly. Reenter one number[Type exit to finish]: ")

def fibonacci(num):
    f_list = []
    for i in range(0, num):
        if i==0:
            f_list.append(1)
        else:
            f_list.append(sum(f_list[i-2:i]) if len(f_list)>1 else sum(f_list))
    return f_list

print(fibonacci(get_interger_input()))