"""A broken implementation of a recursive search for the optimal path through
   a grid of weights.
   Richard Lobb, January 2019.
"""
INFINITY = float('inf')  # Same as math.inf

def read_grid(filename):
    """Read from the given file an n x m grid of integer weights.
       The file must consist of n lines of m space-separated integers.
       n and m are inferred from the file contents.
       Returns the grid as an n element list of m element lists.
       THIS FUNCTION DOES NOT HAVE BUGS.
    """
    with open(filename) as infile:
        lines = infile.read().splitlines()

    grid = [[int(bit) for bit in line.split()] for line in lines]
    return grid


def grid_cost(grid):
    """The cheapest cost from row 1 to row n (1-origin) in the given
       grid of integer weights.
    """
    n_rows = len(grid)
    n_cols = len(grid[0])
    
##    def memoise(f):
##    """ Return a memoised version of function f """
##        known = {}
##        def new_func(*params):
##            if params not in known:
##                known[params] = f(*params)
##            return known[params]
##        return new_func
    table = [n_cols * [0] for row in range(n_rows)]

    
    def cell_cost(row, col):
        """The cost of getting to a given cell in the current grid."""
        if row < 0 or row >= n_rows or col < 0 or col >= n_cols:
            return INFINITY  # Off-grid cells are treated as infinities

        elif row == 0:
            table[row][col] = grid[row][col]
            return grid[row][col]
        
        elif table[row][col] != 0:
            return table[row][col]
        
        else:
            cost = grid[row][col]
##            if row != 0:
            cost += min(cell_cost(row - 1, col + delta_col) for delta_col in range(-1, +2))
            table[row][col] = cost
            
            return table[row][col]

    
    best = min(cell_cost(n_rows - 1, col) for col in range(n_cols))
##    print(table)
    return best
    
    
def file_cost(filename):
    """The cheapest cost from row 1 to row n (1-origin) in the grid of integer
       weights read from the given file
    """
    return grid_cost(read_grid(filename))




##print(file_cost('checkerboard.medium.in.txt'))















"""A broken implementation of a recursive search for the optimal path through
   a grid of weights.
   Richard Lobb, January 2019.
"""
INFINITY = float('inf')  # Same as math.inf

def read_grid(filename):
    """Read from the given file an n x m grid of integer weights.
       The file must consist of n lines of m space-separated integers.
       n and m are inferred from the file contents.
       Returns the grid as an n element list of m element lists.
       THIS FUNCTION DOES NOT HAVE BUGS.
    """
    with open(filename) as infile:
        lines = infile.read().splitlines()

    grid = [[int(bit) for bit in line.split()] for line in lines]
    return grid


def grid_cost(grid):
    """The cheapest cost from row 1 to row n (1-origin) in the given
       grid of integer weights.
    """
    n_rows = len(grid)
    n_cols = len(grid[0])

    table = [n_cols * [0] for row in range(n_rows)]
   
        
     
    for i in range(n_rows):  # For each row
        for j in range(n_cols):   # For each column
            # Evaluate the recurrence equation to fill in the table value.
            if i == 0:
                table[i][j] = grid[i][j]
                
            else:
                cost = grid[i][j]
                temp = []
                for z in range(-1, +2):
                    if j + z >= 0 and j + z < n_cols:
                        temp.append(table[i-1][j+z])
                        
                cost += min(temp)
                table[i][j] = cost
            
                          
    best = min(table[n_rows - 1])
    return best
    
    
def file_cost(filename):
    """The cheapest cost from row 1 to row n (1-origin) in the grid of integer
       weights read from the given file
    """
    return grid_cost(read_grid(filename))



##print(file_cost('checkerboard.medium.in.txt'))










##def coins_reqd(value, coinage):
##    """Minimum number of coins to represent value.
##       Assumes there is a 1-unit coin."""
##    num_coins = [0] * (value + 1)
##    for amt in range(1, value + 1):
##        num_coins[amt] = 1 + min(num_coins[amt - c] for c in coinage if c <= amt)
##        print(num_coins[amt])
##    # The value of the num_coins array is displayed at this point.
##    return num_coins[value]
##
##
##
##print(coins_reqd(19, [1,5,7,11]))

def coins_reqd(value, coinage):
    """Minimum number of coins to represent value"""
    num_coins = [0] * (value + 1)
    best_coins = [0 for i in range(value + 1)]

    for amt in range(1, value + 1):
        minimum = None
        backtrack = None
        for c in coinage:
            if c <= amt:
                coin_count = num_coins[amt - c]  # Num coins required to solve for amt - c
##                print(amt,c)
                if minimum is None or coin_count < minimum:
                    minimum = coin_count
                    backtrack = c
                    
        num_coins[amt] = 1 + minimum
        best_coins[amt] = backtrack
    print(best_coins)
    
    amt = value
    coin_counts = {coin: 0 for coin in coinage}
    
    while amt > 0:
        new_coin = best_coins[amt]
        coin_counts[new_coin] += 1
        amt -= new_coin
        
##    print(coin_counts)
    
    res = [(coin, coin_counts[coin]) for coin in coin_counts if coin_counts[coin] > 0]
    res = sorted(res, reverse=True)
    
    return res


print(coins_reqd(32, [1, 10, 25]))
