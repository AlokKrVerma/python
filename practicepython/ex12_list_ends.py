def modify_list(sample_list):
    return [ sample_list[:1] + sample_list[-1:] if len(sample_list) > 2 else sample_list ]

list_input = [2,3,4,5,6,5,4,3,2.3]

print(modify_list(list_input))



