def list_remove_duplicates(f_list):
    return list(set(f_list))

a = [1,1,2,2,3,3,4,4,5,6,7,8,9]

print(list_remove_duplicates(a))