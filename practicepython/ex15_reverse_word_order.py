def get_string_input():
    org_str = str(input("Please enter one sentence: "))

# Validate
    while len(org_str) == 0 or not isinstance(org_str, str):
        org_str = str(input(" You haven't entered sentence correctly. Please re-enter: "))

    return org_str

[ print(i, end=" ") for i in get_string_input().split(" ")[-1::-1] ]