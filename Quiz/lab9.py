class Item:
    """An item to (maybe) put in a knapsack. Weight must be an int."""
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __repr__(self):
        """The representation of an item"""
        return f"Item({self.value}, {self.weight})"

cached = {}

def max_value(items, capacity):
    """
    Calculates the maximum value of items with a limited capacity
    using top-down recursion and memoisation
    """
    i = len(items)
    if i == 0:
        return 0
        
    elif (i, capacity) in cached:
        return cached[(i, capacity)]

    else:
        if items[i-1].weight > capacity:
            cached[(i, capacity)] = max_value(items[:-1], capacity)

        else:
            value1 = max_value(items[:-1], capacity)
            value2 = max_value(items[:-1], capacity - items[-1].weight) + items[-1].value
            cached[(i, capacity)] = max(value1, value2)


    return cached[(i, capacity)]


## The example from the lecture notes
##items = [
##Item(45, 3),
##Item(45, 3),
##Item(80, 4),
##Item(80, 5),
##Item(100, 8)]
##print(max_value(items, 10))
##print(cached)
	
## A large problem (500 items)
##import random
##random.seed(12345)  # So everyone gets the same
##items = [Item(random.randint(1, 100), random.randint(1, 100)) for i in range(500)]
##print(max_value(items, 500))










##def fractional_knapsack(capacity, items):
##    """
##    Returns the maximum value of items in a limited capacity knapsack
##    when you're allowed parts of items
##    """
##    items.sort(key = lambda x: x[1]/x[2], reverse = True)
##    current_weight = 0
##    value = 0
##
##    for (item, it_value, it_weight) in items:
##        weight_dif = capacity - current_weight
##        if weight_dif > 0:
##            if weight_dif >= it_weight:
##                value += it_value
##                current_weight += it_weight
##            else:
##                ratio = weight_dif/it_weight
##                value += it_value * ratio
##                current_weight += it_weight * ratio
##    
##    return value









##items = [Item(45, 3),
##         Item(45, 3),
##         Item(80, 4),
##         Item(80, 5),
##         Item(100, 8)]
##for capacity in range(26):
##    print(f"{capacity:2}: {max_value(items, capacity)}")
    
### The example in the lecture notes
##items = [Item(45, 3),
##Item(45, 3),
##Item(80, 4),
##Item(80, 5),
##Item(100, 8)]
##print(max_value(items, 10))
class Item:
    """An item to (maybe) put in a knapsack"""
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        
    def __repr__(self):
        return f"Item({self.value}, {self.weight})"

    



def max_value(items, capacity):
    """The maximum value achievable with a given list of items and a given
    knapsack capacity."""
##    table = []
##    for i in range(len(items) + 1):
##        table += [[0] * capacity]
    
    grid = [[0 for j in range(capacity + 1)] for i in range(len(items) + 1)]
##    print(grid)
    for i in range(len(grid)):        
        for j in range(len(grid[0])):
            if i == 0 or j == 0:
                grid[i][j] = 0
                
            elif items[i-1].weight <= j:
                grid[i][j] = max(items[i-1].value + grid[i-1][j - items[i-1].weight], grid[i-1][j])

            else:
                grid[i][j] = grid[i-1][j]
                
##    print(grid)
    
    res = grid[i][j]
    res_list = []

    while i > 0 and j > 0:
##        print(grid[i][j], grid[i-1][j])
##        print(i,j)
        if grid[i][j] != grid[i-1][j]:
            res_list.append(items[i-1])
            j -= items[i-1].weight

        i -= 1
        
##    print(res_list)
    return res, res_list

    
##    result = grid[-1][-1]
##    cap = capacity
##    n = len(items)
##    items_used = []
##    for i in range(n, 0, -1):
##        if result <= 0:
##            break
##        if result == grid[i - 1][cap]:
##            continue
##        else:
##            items_used.append(items[i - 1])
##            result = result - items[i-1].value
##            cap = cap - items[i-1].weight
##
##    return grid[-1][capacity], items_used




#### The example in the lecture notes
##items = [Item(45, 3),
##         Item(45, 3),
##         Item(80, 4),
##         Item(80, 5),
##         Item(100, 8)]
##maximum, selected_items = max_value(items, 10)
##print(maximum)
# Check the returned item list with a hidden function
##check_item_list(items, selected_items, maximum)






def lcs(s1, s2):
##    grid = [[0] * (len(s2) + 1) for i in range(len(s1) + 1)]

    dic = {}
    def cache(s1, s2):
        if s1 == '' or s2 == '':
            return ''
        
        elif (s1, s2) in dic:
            return dic[(s1, s2)]
        
        elif s1[-1] == s2[-1]: # Last chars match
            dic[(s1, s2)] = cache(s1[:-1], s2[:-1]) + s1[-1]
            
        else:
            # Drop last char of each string in turn.
            # Choose best outcome. 
            soln1 = cache(s1[:-1], s2)
            soln2 = cache(s1, s2[:-1])

            if len(soln1) > len(soln2):
                dic[(s1, s2)] = soln1
            else:
                dic[(s1, s2)] = soln2
  
        return dic[(s1, s2)]


    return cache(s1, s2)









def lcs(s1, s2):
##    grid = [[0] * (len(s2) + 1) for i in range(len(s1) + 1)]

    dic = {}
    def cache(s1, s2):
        if s1 == '' or s2 == '':
            dic[(s1, s2)] = ''
        
        elif (s1, s2) in dic:
            pass
        
        elif s1[-1] == s2[-1]: # Last chars match
            dic[(s1, s2)] =  cache(s1[:-1], s2[:-1]) + s1[-1]
            
        else:
            # Drop last char of each string in turn.
            # Choose best outcome. 
            soln1 = cache(s1[:-1], s2)
            soln2 = cache(s1, s2[:-1])
            if len(soln1) > len(soln2):
                dic[(s1, s2)] = soln1
            else:
                dic[(s1, s2)] = soln2
                
        return dic[(s1, s2)]

##    print(s1, s2)
    return cache(s1, s2)

## A simple test that should run without caching

##s1 = 'ZEPM'
##s2 = 'EHME'
##
##lcs_string = lcs(s1, s2)
##print(lcs_string)


##s1 = 'TROJAN'
##s2 = 'TIJUANA'
##
##lcs_string = lcs(s1, s2)
##print(lcs_string)


##s1 = "abcde"
##s2 = "qbxxd"
##lcs_string = lcs(s1, s2)
##print(lcs_string)
##
##
##s1 = "Look at me, I can fly!"
##s2 = "Look at that, it's a fly"
##print(lcs(s1, s2))
##
##s1 = "abcdefghijklmnopqrstuvwxyz"
##s2 = "ABCDEFGHIJKLMNOPQRSTUVWXYS"
##print(lcs(s1, s2))
##s1 = "balderdash!"
##s2 = "balderdash!"
##print(lcs(s1, s2))



#####special case
##def cost(a, b, na=None, nb=None):
##    """ Cost of converting first na chars of a into first nb chars of b """
##    if na is None:  # Top level call - both na and nb will be None
##        na = len(a)
##        nb = len(b)
##    if na == 0 or nb == 0:
##        # One string is empty - n insertions or deletions required
##        return max(na, nb) 
##    elif a[na - 1] == b[nb - 1]:  # Do last chars match?
##        return cost(a, b, na - 1, nb - 1)  # Yes - this is the align/copy case
##    else:  # Last chars don't match
##        # Must delete last a, insert last b or replace last a with last b
##        delete_cost = 1 + cost(a, b, na - 1, nb)
##        insert_cost = 1 + cost(a, b, na, nb - 1)
##        replace_cost = 1 + cost(a, b, na - 1, nb - 1)
####        print(delete_cost, insert_cost, replace_cost)
##        return min(delete_cost, insert_cost, replace_cost)
####
####
######print(cost('GATCG', 'ATCTCCG'))
####print(cost('THEM', 'TIM'))
####print(cost('ROCKER', 'FRECKLE'))
##print(cost('Delicious', 'Dalhousie'))




##cached = {}
##
##def max_value(items, capacity):
##    """
##    Calculates the maximum value of items with a limited capacity
##    using top-down recursion and memoisation
##    """
##    i = len(items)
##    if i == 0:
##        return 0
##        
##    elif (i, capacity) in cached:
##        return cached[(i, capacity)]
##
##    else:
##        if items[i-1].weight > capacity:
##            cached[(i, capacity)] = max_value(items[:-1], capacity)
##
##        else:
##            value1 = max_value(items[:-1], capacity)
##            value2 = max_value(items[:-1], capacity - items[-1].weight) + items[-1].value
##            cached[(i, capacity)] = max(value1, value2)
##
####    print(cache)
##    return cached[(i, capacity)]




cached = {}

def cost(a, b, na=None, nb=None):
    if na is None or nb is None:
        na = len(a)
        nb = len(b)

    if na == 0 or nb == 0:
        return max(na, nb)



    key = na, nb
    if key in cached:
        return cached[key]

    elif a[na - 1] == b[nb - 1]:
        cached[key] = cost(a, b, na - 1, nb - 1)


    else:  # Last chars don't match
        delete_cost = 1 + cost(a, b, na - 1, nb)
        insert_cost = 1 + cost(a, b, na, nb - 1)
        replace_cost = 1 + cost(a, b, na - 1, nb - 1)

        cached[key] = min(delete_cost, insert_cost, replace_cost)
        
    return cached[key]

print(cost('Delicious', 'Dalhousie'))
print(cached)



