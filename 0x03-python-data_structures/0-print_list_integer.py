def print_list_integer(my_list=None):
    if my_list is None:
        my_list = []  # Create an empty list if no list is provided
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
