def key_positions(seq, key):
    key_list = []
    for i in seq:
        key_list.append(key(i))

##    print(key_list)
    
    k = max(key_list)
    res = [0] * (k + 1)
    
    for num in key_list:
        res[num] = res[num] + 1

    count = 0
    for index in range(len(res)):
        res[index], count = count, count + res[index]

    return res


##print(key_positions([0, 1, 2], lambda x: x))
##print(key_positions([2, 1, 0], lambda x: x))
##print(key_positions([1, 2, 3, 2], lambda x: x))
##print(key_positions([5], lambda x: x)) 
##print(key_positions(range(-3,3), lambda x: x**2))
##print(key_positions(range(1000), lambda x: 4))
##print(key_positions([1] + [0] * 100, lambda x: x))



##def sorted_array(seq, key, positions):
##    res = [None] * len(seq)
##    
##    for i in seq:
##        key_value = key(i)
##        index = positions[key_value]
##
##        while res[index] != None:
##            index += 1
##        res[index] = i
##
##    return res
##
##
##
##def key_positions(seq, key):
##    key_list = []
##    for i in seq:
##        key_list.append(key(i))
##        
##    k = max(key_list)
##    res = [0] * (k + 1)
##    
##    for num in key_list:
##        res[num] = res[num] + 1
##
##    count = 0
##    for index in range(len(res)):
##        res[index], count = count, count + res[index]
##
##    return res
##
##
##
##def sorted_array(seq, key, positions):
##    res = [None] * len(seq)
##    
##    for i in seq:
##        res[positions[key(i)]] = i
##        positions[key(i)] = positions[key(i)] + 1
##
##    return res
##
##
##
##print(sorted_array([3, 1, 2], lambda x: x, [0, 0, 1, 2]))
##print(sorted_array([3, 2, 2, 1, 2], lambda x: x, [0, 0, 1, 4])) 
##print(sorted_array([100], lambda x: x, [0]*101)) 
##
##
##"""Counting Sort"""
##import operator
##def counting_sort(iterable, key):
##    positions = key_positions(iterable, key)
##    return sorted_array(iterable, key, positions)
##objects = [("a", 88), ("b", 17), ("c", 17), ("d", 7)]
##key = operator.itemgetter(1)
##print(", ".join(object[0] for object in counting_sort(objects, key)))




##def key_positions(seq, key):
##    key_list = []
##    for i in seq:
##        key_list.append(key(i))
##
##    k = max(key_list)
##    res = [0] * (k + 1)
##
##    for num in key_list:
##        res[num] = res[num] + 1
##
##    count = 0
##    for index in range(len(res)):
##        res[index], count = count, count + res[index]
##
##    return res
##
##
##
def sorted_array(seq, key):
    res = [None] * len(seq)
    positions = key_positions(seq, key)

    for i in seq:
        res[positions[key(i)]] = i
        positions[key(i)] = positions[key(i)] + 1

    return res

##print(key_positions([2, -2, 1], lambda x: x**2))
##print(sorted_array([2, -2, 1], lambda x: x**2))







def radix_sort(numbers, d):
    max_len = len(str(max(numbers)))
    numbers = [str(x) for x in numbers]

    for i in range(len(numbers)):
        if len(numbers[i]) < max_len:
            numbers[i] = "0" * (max_len - len(numbers[i])) + numbers[i]

    index = 1
    for i in range(d):
        if index <= d:
            numbers = sorted_array(numbers, key=lambda x: int(x[-index]))
        index += 1

    res = [int(x) for x in numbers]
    return res


##def radix_sort(numbers, d):
##    max_len = len(str(max(numbers)))
##    numbers = [str(x) for x in numbers]
##
##    for i in range(len(numbers)):
##        if len(numbers[i]) < max_len:
##            numbers[i] = "0" * (max_len - len(numbers[i])) + numbers[i]
##            
##    num = -1
##    while num >= -d:
##        numbers = sorted_array(numbers, lambda x: int(x[num]))
##        num -= 1
##
##    res = [int(x) for x in numbers]
##    return res



print(radix_sort([329, 457, 657, 839, 436, 720, 355], 3))
##print(radix_sort([329, 457, 657, 839, 436, 720, 355], 1))
##print(radix_sort([329, 457, 657, 839, 436, 720, 355], 2))
##print(radix_sort([9, 57, 657], 2))
