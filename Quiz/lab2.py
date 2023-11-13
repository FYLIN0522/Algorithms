##def cycle_length(n):
##    if n == 1:
##        return 1
##
##    else:
##        if n % 2 == 0:
##            return 1 + cycle_length(n/2)
##
##        return 1 + cycle_length(3*n+1)
##
##
##print(cycle_length(22)) 
##if prohibited_constructs_are_used():
##    print("Your code contains some form of loop (for, while, list comprehension, ...)")
##    print("or is importing a module.")
##else:
##    print("OK")





##def recursive_divide(x, y):
##    if x - y < 0:
##        return 0
##    
##    else:
##        return 1 + recursive_divide(x - y, y)
##
##
##print(recursive_divide(8, 3))




##def my_enumerate(items, index=0):
##    if index >= len(items):
##        return []
##
##    else:
##        return [(index, items[index])] + my_enumerate(items, index + 1)
##
##
##ans = my_enumerate([10, 20, 30])
##print(ans)
##
##ans = my_enumerate(['dog', 'pig', 'cow'])
##print(ans)
##
##ans = my_enumerate([])
##print(ans)





##def num_rushes(slope_height, rush_height_gain, back_sliding, start_height=0):
##    start_height += rush_height_gain
##    if start_height >= slope_height:
##        return 1
##
##    else:
##        start_height -= back_sliding
##        return 1 + num_rushes(slope_height, rush_height_gain, back_sliding, start_height)
##
##
##ans = num_rushes(10, 10, 9)
##print(ans)
##
##ans = num_rushes(100, 10, 0)
##print(ans)
    




##def num_rushes(slope_height, rush_height_gain, back_sliding, start_height=0):
##
##    start_height += rush_height_gain
##    
##    if start_height >= slope_height:
##        return 1
##
##    else: 
##        start_height -= back_sliding
##        return 1 + num_rushes(slope_height, rush_height_gain * 0.95, back_sliding *0.95, start_height)
##
##
##
##ans = num_rushes(100, 15, 7)
##print(ans)
##
##ans = num_rushes(10, 10, 9)
##print(ans)
##	
##ans = num_rushes(150,20,9)
##print(ans)





##import sys
##sys.setrecursionlimit(100000)
##def dumbo_func(data):
##    """Takes a list of numbers and does weird stuff with it"""
##    if len(data) == 0:
##        return 0
##    else:
##        if (data[0] // 100) % 3 != 0:
##            return 1 + dumbo_func(data[1:])
##        else:
##            return dumbo_func(data[1:])
##
##import sys
##sys.setrecursionlimit(100000)
##
##
##def dumbo_func(data, index=0):
##    """Takes a list of numbers and does weird stuff with it"""
##    if index >= len(data):
##        return 0
##    
##    else:
##        if (data[index] // 100) % 3 != 0:
##            return 1 + dumbo_func(data, index + 1)
##        else:
##            return dumbo_func(data, index + 1)
##
## Simple test with short list.
## Original func works fine on this
##data = [677, 90, 785, 875, 7, 90393, 10707]
##data = []
##for i in range(2000):
##    data.append(i)
##print(dumbo_func(data))






##def fib(n):
##    if n == 0:
##        return 0
##    
##    elif n == 1:
##        return 1
##
##    else:
##        return fib(n-1) + fib(n-2)
##    
##print(fib(5))
##print(fib(6))
##print(fib(7))
##print(fib(100))





def fib(n):
    if n < 2:
        return n

    q = [[1, 1], [1, 0]]
    res = matrix_pow(q, n - 1)
    return res[0][0]



def matrix_pow(a, n):
    ret = [[1, 0], [0, 1]]
    while n > 0:
        if n % 2 == 1:
            ret = matrix_multiply(ret, a)
        n = int(n / 2)
        a = matrix_multiply(a, a)
    return ret



def matrix_multiply(a, b):
    c = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j]

    return c


print(fib(5))
print(fib(6))
print(fib(7))
print(fib(8))
print(fib(100))





##class Solution {
##    public int fib(int n) {
##        //矩阵快速幂
##
##        if (n < 2) {
##            return n;
##        }
##
##        //定义乘积底数
##        int[][] base = {{1, 1}, {1, 0}};
##
##        //定义幂次
##        int power = n - 1;
##
##        int[][] ans = calc(base, power);
##
##        //按照公式，返回的是两行一列矩阵的第一个数
##        return ans[0][0];
##    }
##
##    //定义函数,求底数为 base 幂次为 power 的结果
##    public int[][] calc(int[][] base, int power) {
##
##        //定义变量，存储计算结果，此次定义为单位阵
##        int[][] res = {{1, 0}, {0, 1}};
##
##        //可以一直对幂次进行整除
##        while (power > 0) {
##
##            //1.若为奇数，需多乘一次 base
##            //2.若power除到1，乘积后得到res
##            //此处使用位运算在于效率高
##            if ((power & 1) == 1) {
##
##                res = mul(res, base);
##
##            }
##
##            //不管幂次是奇还是偶，整除的结果是一样的如 5/2 和 4/2
##            //此处使用位运算在于效率高
##            power = power >> 1;
##
##            base = mul(base, base);
##        }
##
##        return res;
##    }
##
##    //定义函数,求二维矩阵：两矩阵 a, b 的乘积
##    public int[][] mul(int[][] a, int[][] b) {
##
##        int[][] c = new int[2][2];
##
##        for (int i = 0; i < 2; i++) {
##
##            for (int j = 0; j < 2; j++) {
##
##                //矩阵乘积对应关系，自己举例演算一遍便可找到规律
##                c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j];
##
##            }
##        }
##
##        return c;
##    }
##}
    
    

    
