from pprint import pprint

def adjacency_list(graph_str):
    graph_str = graph_str.replace("\n"," ")
    graph_str = graph_str.split(" ")
    graph_str.pop()
    empty_list = []
    length = len(graph_str)
    for i in range(int(graph_str[1])):
        empty_list.append([])


    
    if graph_str[2] == 'W':
        j = 3
        
        while j <= length - 3:
            j_E = graph_str[j + 1]
            j_W = graph_str[j + 1 + 1]
            
            empty_list[int(graph_str[j])] += [(int(j_E), int(j_W))]
            
            if graph_str[0] == 'U':
                empty_list[int(j_E)] += [(int(graph_str[j]), int(j_W))]

            
            j += 3
            j_E = 0
            j_W = 0


    else:
        j = 2
        
        while j <= length - 2:
            j_E = graph_str[j + 1]
            empty_list[int(graph_str[j])] += [(int(j_E), None)]


            if graph_str[0] == 'U':
                empty_list[int(j_E)] += [(int(graph_str[j]), None)]
                
            j += 2
            j_E = 0
    return empty_list


def bfs_tree(adj_list, start):
    length = len(adj_list)
    n = adj_list
    state = ['U'] * length
    parent = [None] * length
    q = []
    state[start] = 'D'
    q.append(start)
    return bfs_loop(n, q, state, parent)



def bfs_loop(n, q, state, parent):
    while q != []:
        u = q.pop(0)
        for v in n[u]:
            if state[v[0]] == 'U':
                state[v[0]] = 'D'
                parent[v[0]] = u
                q.append(v[0])
        state[u] = 'P'
        
    return state

        
def dfs_tree(adj_list, start):
    length = len(adj_list)
    n = adj_list
    state = ['U'] * length
    parent = [None] * length
    state[start] = 'D'
    dfs_loop(n, start, state, parent)
    
    return state



def dfs_loop(n, u, state, parent):
    for v in n[u]:
        if state[v[0]] == 'U':
            state[v[0]] = 'D'
            parent[v[0]] = u
            dfs_loop(n, v[0], state, parent)

    state[u] = 'P'
        


def transpose(adj_list):
##    list_t = [[]] * len(adj_list)
    list_t = []
    for length in range(len(adj_list)):
        list_t.append([])
    index = 0

    for i in adj_list:
##        if len(graph_string) >= 5 and graph_string[4] == 'W':
##        if len(list_t) >= 4 and list_t[3] == 'W':
        for j in i:
            temp = (index, j[1])
            list_t[j[0]].append(temp)
                
##        else:
##            for j in i:
##                temp = (index, j[1])
##                list_t[j[0]].append(temp)
                
        index += 1

    return list_t



def is_strongly_connected(adj_list):
    for start in range(len(adj_list)):
        list_g = bfs_tree(adj_list, start)
##        print(list_g)
        if 'U' in list_g:
            return False
    
    for start in range(len(adj_list)):
        list_gt = transpose(adj_list)
        list_gt = bfs_tree(adj_list, start)
##        print(list_gt)
        if 'U' in list_gt:
            return False

    return True





####Q3
##graph_string = """\
##D 3
##0 1
##1 0
##0 2
##"""
##
##print(is_strongly_connected(adjacency_list(graph_string)))
####
##graph_string = """\
##D 3
##0 1
##1 2
##2 0
##"""
##
##print(is_strongly_connected(adjacency_list(graph_string)))
##
##graph_string = """\
##D 4
##0 1
##1 2
##2 0
##"""
##
##print(is_strongly_connected(adjacency_list(graph_string)))
##
### Since we are passing an adjacency list to your algorithm,
### it will see an un directed graph as a directed one where each
### undirected edge appears as two directed edges.
##
##graph_string = """\
##U 5
##2 4
##3 1
##0 4
##2 1
##"""
##
##print(is_strongly_connected(adjacency_list(graph_string)))
##
##graph_string = """\
##D 6
##0 1
##1 2
##2 0
##3 4
##4 5
##5 3
##2 4
##"""
##
##print(is_strongly_connected(adjacency_list(graph_string)))





####Q2
##graph_string = """\
##D 3
##0 1
##1 0
##0 2
##"""
####transpose(adj_list)
##graph_adj_list = adjacency_list(graph_string)
##graph_transposed_adj_list = transpose(graph_adj_list)
##for i in range(len(graph_transposed_adj_list)):
##    print(i, sorted(graph_transposed_adj_list[i]))
##    
##graph_string = """\
##D 3 W
##0 1 7
##1 0 -2
##0 2 0
##"""
##graph_adj_list = adjacency_list(graph_string)
##graph_transposed_adj_list = transpose(graph_adj_list)
##for i in range(len(graph_transposed_adj_list)):
##    print(i, sorted(graph_transposed_adj_list[i]))
##
#### It should also work undirected graphs.
#### The output will be the same as input.
##graph_string = """\
##U 7
##1 2
##1 5
##1 6
##2 3
##2 5
##3 4
##4 5
##"""
##graph_adj_list = adjacency_list(graph_string)
##graph_transposed_adj_list = transpose(graph_adj_list)
##for i in range(len(graph_transposed_adj_list)):
##    print(i, sorted(graph_transposed_adj_list[i]))
##
##graph_string = """\
##U 17
##1 2
##1 15
##1 6
##12 13
##2 15
##13 4
##4 5
##"""
##graph_adj_list = adjacency_list(graph_string)
##graph_transposed_adj_list = transpose(graph_adj_list)
##for i in range(len(graph_transposed_adj_list)):
##    print(i, sorted(graph_transposed_adj_list[i]))




##from math import inf
##def next_vertex(in_tree, distance):
##    total_dis = 0
##    index = 0
##
##    for i in in_tree:
##        if i is True:
##            total_dis += distance[index]
##            index += 1
##            
##    sort_distance = sorted(distance)
##    next_vertex_dis = sort_distance[index]
##    next_vertex = distance.index(next_vertex_dis)
##    s = in_tree[next_vertex]
##    while s:
##        s = in_tree[next_vertex + 1]
##        next_vertex += 1
##        if next_vertex_dis != distance[next_vertex] and s is False:
##            s = True
####        if next_vertex_dis < distance[next_vertex]:
####            s = in_tree[next_vertex + 1]
####            next_vertex += 1
##        
##    return next_vertex
##in_tree = [False, True, True, False, False]
##distance = [float('inf'), 0, 3, 12, 5]
##print(next_vertex(in_tree, distance))
##
##in_tree = [False, False, False]
##distance = [float('inf'), 0, float('inf')]
##print(next_vertex(in_tree, distance))
##
##in_tree = [True, True, True, False, True]
##distance = [inf, 0, inf, inf, inf]
##print(next_vertex(in_tree, distance))
##
##in_tree = [True, False, False, True]
##distance = [3, 5, 3, 0]
##print(next_vertex(in_tree, distance))

##from math import inf
##def dijkstra(adj_list, start):
####    print(adj_list)
##    n = adj_list
##    in_tree = [False] * len(adj_list)
##    distance = [float('inf')] * len(adj_list)
##    parent = [None] * len(adj_list)
##    distance[start] = 0
##    
##    while False in in_tree:
##        u = next_vertex(in_tree, distance)
##        in_tree[u] = True
##        
##        for v,weight in n[u]:
##            if in_tree[v] is False and distance[u] + weight < distance[v]:
##                distance[v] = distance[u] + weight
##                parent[v] = u
##
##    return parent,distance








##Q15
from math import inf
def next_vertex(in_tree, distance):
    total_dis = 0
    index = 0

    for i in in_tree:
        if i is True:
            total_dis += distance[index]
            index += 1
            
    sort_distance = sorted(distance)
    next_vertex_dis = sort_distance[index]
    next_vertex = distance.index(next_vertex_dis)
    s = in_tree[next_vertex]
    
    while s:
        s = in_tree[next_vertex + 1]
        next_vertex += 1


        if next_vertex_dis != distance[next_vertex] and s is False:
            s = True
##        else:
##            s = in_tree[next_vertex + 1]
##            next_vertex += 1
##        if next_vertex_dis < distance[next_vertex]:
##            s = in_tree[next_vertex + 1]
##            next_vertex += 1
            
    return next_vertex
##
##
##



def dijkstra(adj_list, start):
    n = adj_list
    in_tree = [False] * len(adj_list)
    distance = [float('inf')] * len(adj_list)
    parent = [None] * len(adj_list)
    distance[start] = 0
    
    while False in in_tree:
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        for v,weight in n[u]:
            if in_tree[v] is False and (distance[u] + weight) < distance[v]:
                distance[v] = distance[u] + weight
                parent[v] = u

    return parent, distance

graph_string = """\
D 3 W
1 0 3
2 0 1
1 2 1
"""
print(dijkstra(adjacency_list(graph_string), 1))
print(dijkstra(adjacency_list(graph_string), 2))
##
##graph_string = """\
##U 4 W
##0 2 5
##0 3 2
##3 2 2
##"""
##
##print(dijkstra(adjacency_list(graph_string), 0))
##print(dijkstra(adjacency_list(graph_string), 2))
##
##graph_string = """\
##U 5 W
##0 1 1
##1 2 5
##2 3 1
##3 4 1
##4 0 1
##"""
##
##print(dijkstra(adjacency_list(graph_string), 0))






def next_vertex(in_tree, distance):
    res = []
    
    for i in range(len(in_tree)):
        if in_tree[i] == False:
            res.append((i, distance[i]))
    print(res)

    min_vex = res[0][1]
    next_vex = res[0][0]
    
    for j in res:
        if j[1] < min_vex:
            min_vex = j[1]
            next_vex = j[0]
        
    return next_vex
##
##    
##in_tree = [False, True, True, False, False]
##distance = [float('inf'), 0, 3, 12, 5]
##print(next_vertex(in_tree, distance))

