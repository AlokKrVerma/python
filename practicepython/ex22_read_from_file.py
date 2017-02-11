name_count = {}

with open("Ex22_file.txt", 'r') as file_read:
    for name in file_read.readlines():
        name = name.replace("\n", '') #handle new lines char
        if name in name_count:
            name_count[name] += 1
        else:
            name_count[name] = 1

for key in name_count.keys():
    print(" {} has {} entries in file".format(key, name_count[key]))
