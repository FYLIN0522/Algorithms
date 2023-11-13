##def change_greedy(amount, coinage):
##    """1"""
##    res = []
##    sort_coinage = sorted(coinage, reverse=True)
##    
##    for i in sort_coinage:
##        num_coin = int(amount / i)
##        if num_coin > 0:
##            res.append((num_coin, i))
##
##        amount -= num_coin * i
##
##    if amount != 0:
##        return None
##    
##    return res
##
##
##
##
##print(change_greedy(82, [1, 10, 25, 5]))
##print(change_greedy(80, [1, 10, 25]))
##print(change_greedy(82, [10, 25, 5]))




##def print_shows(show_list):
##    s = []
##    sorted_show_list = sorted(show_list, key=lambda show_list : show_list[1] + show_list[2])
##    time_current = 0
####    print(sorted_show_list)
##    for i in sorted_show_list:
##        
##        if i[1] >= time_current:
##            time_current = i[1] + i[2]
####            s.append((i[0], i[1], time_current))
##            print(i[0], i[1], time_current)
##    
####    return s
##
##
##print_shows([
##('a', 0, 6),
##('b', 1, 3),
##('c', 3, 2),
##('d', 3, 5),
##('e', 4, 3),
##('f', 5, 4),
##('g', 6, 4),
##('h', 8, 3)])





def fractional_knapsack(capacity, items):
    value = 0
    sorted_items = sorted(items, reverse=True, key=lambda items : items[1] / items[2])
##    print(sorted_items)
    
    for i in sorted_items:
        if capacity - i[2] >= 0:
            capacity -= i[2]
            value += i[1]
            
        else:
            while capacity > 0:
                capacity -= 1
                value += i[1]/i[2]

    return value

items = [
    ("Chocolate cookies", 20, 5),
    ("Potato chips", 15, 3),
    ("Pizza", 14, 2),
    ("Popcorn", 12, 4)]
print(fractional_knapsack(9, items))
