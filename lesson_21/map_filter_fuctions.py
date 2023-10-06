def int_check(item):
    if item == int(item):
        return True
    return False


"""
'map' 
"""
random_list1 = [1, 'dhd', 5.78, 4, 97, 56, 'gfj']
str_values_list = list(map(str, random_list1))
print(str_values_list)

"""
'filter' with external check function
"""
random_list2 = [1, 56.8, 25.805, 665756.85, 5, 65, 5687]
int_values_list = list(filter(int_check, random_list2))
print(int_values_list)

"""
'filter' with lambda function
"""
int_values_list_1 = list(filter(lambda item: item == int(item), random_list2))
print(int_values_list_1)
