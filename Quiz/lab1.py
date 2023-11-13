##def almost_all(numbers):
##    total = sum(numbers)
##    return [total - x for x in numbers]



def foo(numbers):
    length = len(numbers) - 1
    result = []
    last_index = length

    for i in range(length, -1, -1):
        if last_index == i:
            result.append(numbers[i])
        
        elif numbers[i] < numbers[last_index]:
            result.append(numbers[i])
            last_index = i
        
        else:
            result.append(numbers[last_index])

    return result[::-1]
    

print(foo([1, 2, 3, 3]))

print(foo([2, 4, 5, 3]))

foo(list(range(10**5)))
print("OK")


##def concat_list(strings):
##    if len(strings) == 0:
##        return ""
##    
##    else:
##        return strings[0] + concat_list(strings[1:])




##def product(data):
##    if len(data) == 0:
##        return 1
##
##    else:
##        return data[0] * product(data[1:])




##def backwards(s):
##    index = len(s)
##    if len(s) == 0:
##        return ""
##
##    else:
##        index -= 1
##        return s[-1] + backwards(s[:index])




##def odds(data):
##    if len(data) == 0:
##        return []
##
##    else:
##        if data[0] % 2 == 1:
##            return [data[0]] + odds(data[1:])
##            
##        return odds(data[1:])





##def squares(data):
##    if len(data) == 0:
##        return []
##
##    else:
##        return [data[0] ** 2] + squares(data[1:])





##def find(data, value):
##    if value not in data:
##        return None
##    
##    else:
##        if data[0] == value:
##            return 0
##        
##        else:
##            return 1 + find(data[1:], value)


