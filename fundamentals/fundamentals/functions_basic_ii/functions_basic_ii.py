def countdown(x):
    count_list = []
    if not isinstance(x, int):
        return count_list
    else: 
        for y in range(x, -1, -1):
            count_list.append(y)
        return count_list
print(countdown(5))

def print_and_return(num_list):
    print(num_list[0])
    return num_list[1]
print(print_and_return([1,2]))

def first_plus_length(num_list):
    return num_list[0] + len(num_list)
print(first_plus_length([1,2,3,4,5]))

def greater_than_second(num_list):
    if len(num_list) < 2:
        return False
    greater = []
    for x in num_list:
        if x > num_list[1]:
            greater.append(x)
    print(len(greater))
    return greater
print(greater_than_second([5,2,3,2,1,4]))
print(greater_than_second([3]))

def length_and_value(size, value):
    num_list = []
    for x in range(0, size):
        num_list.append(value)
    return num_list
print(length_and_value(4, 7))
print(length_and_value(6, 2))