from pprint import pprint

##def adjacency_list(graph_str):
##    graph_str = graph_str.replace("\n"," ")
##    graph_str = graph_str.split(" ")
##    graph_str.pop()
##    
##    empty_list = []
##    length = len(graph_str)
##    for i in range(int(graph_str[1])):
##        empty_list.append([])
##
##
##    
##    if graph_str[2] == 'W':
##        j = 3
##        
##        while j <= length - 3:
##            j_E = graph_str[j + 1]
##            j_W = graph_str[j + 1 + 1]
##            
##            empty_list[int(graph_str[j])] += [(int(j_E), int(j_W))]
##            
##            if graph_str[0] == 'U':
##                empty_list[int(j_E)] += [(int(graph_str[j]), int(j_W))]
##
##            
##            j += 3
##            j_E = 0
##            j_W = 0
##
##
##
##    else:
##        j = 2
##        
##        while j <= length - 2:
##            j_E = graph_str[j + 1]
##            empty_list[int(graph_str[j])] += [(int(j_E), None)]
##
##
##            if graph_str[0] == 'U':
##                empty_list[int(j_E)] += [(int(graph_str[j]), None)]
##                
##            j += 2
##            j_E = 0
##    return empty_list



def adjacency_list(graph_str):
##    print(graph_str)
    graph_str = graph_str.splitlines()
##    print(graph_str)
    graph_type = graph_str[0].split()[0]
##    print(graph_str[0].split())
    num_vex = int(graph_str[0].split()[1])
    graph = [[] for i in range(num_vex)]

    
    for i in range(1, len(graph_str)):
        line = graph_str[i].split()
##        print(line)
        weight = None
        vex0 = int(line[0])
        vex1 = int(line[1])
        if len(line) == 3:
            weight = int(line[2])

        graph[vex0].append((vex1, weight))
        if graph_type == 'U':
            graph[vex1].append((vex0, weight))
    
    return graph

##graph_string = """\
##U 5
##0 1
##1 2
##1 3
##3 4
##4 0
##"""
##print(adjacency_list(graph_string))


##graph_string = """\
##U 6
##0 4
##5 4
##4 2
##2 3
##3 0
##3 4
##"""
##print(adjacency_list(graph_string))



##graph_string = """\
##U 12 W
##0 1 1
##1 9 12
##1 10 3
##1 11 -4
##10 11 25
##"""
##
##pprint(adjacency_list(graph_string))
##
##
##
##graph_string = """\
##D 3
##0 1
##1 0
##0 2
##"""
##print(adjacency_list(graph_string))
##
##graph_string = """\
##D 3 W
##0 1 7
##1 0 -2
##0 2 0
##"""
##print(adjacency_list(graph_string))
##
##
### undirected graph in the textbook example
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
##pprint(adjacency_list(graph_string))
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
##pprint(adjacency_list(graph_string))










##from pprint import pprint
##
##def adjacency_matrix(graph_str):
##    graph_str = graph_str.replace("\n"," ")
##    graph_str = graph_str.split(" ")
##    graph_str.pop()
##    empty_list = []
##    length = len(graph_str)
##    
##    if length <= 2:
##        for i in range(int(graph_str[1])):
##            empty_list.append([0] * int(graph_str[1]))
##
##        return empty_list
##
##    
##    elif graph_str[2] == 'W':
##        for i in range(int(graph_str[1])):
##            empty_list.append([None] * int(graph_str[1]))
##
##            
##        j = 3
##        
##        while j <= length - 3:
##            j_E = graph_str[j + 1]
##            j_W = graph_str[j + 1 + 1]
##            
##            empty_list[int(graph_str[j])] [int(j_E)] = int(j_W)
##            
##            if graph_str[0] == 'U':
##                empty_list[int(j_E)] [int(graph_str[j])] = int(j_W)
##
##            
##            j += 3
##            j_E = 0
##            j_W = 0
##
##
##    
##    else:
##        for i in range(int(graph_str[1])):
##            empty_list.append([0] * int(graph_str[1]))
##        j = 2
##        
##        while j <= length - 2:
##            j_E = graph_str[j + 1]
##            empty_list[int(graph_str[j])] [int(j_E)] = 1
##
##
##            if graph_str[0] == 'U':
##                empty_list[int(j_E)] [int(graph_str[j])] = 1
##                
##            j += 2
##            j_E = 0
##    return empty_list


def adjacency_matrix(graph_str):
    graph_str = graph_str.splitlines()
    graph_type = graph_str[0].split()[0]
    num_vex = int(graph_str[0].split()[1])

    graph = []
    if len(graph_str[0].split()) == 3:
        for i in range(num_vex):
            graph.append([None] * num_vex)
            
    else:
        for i in range(num_vex):
            graph.append([0] * num_vex)


    for i in range(1, len(graph_str)):
        line = graph_str[i].split()
        weight = 1
        vex0 = int(line[0])
        vex1 = int(line[1])
        if len(line) == 3:
            weight = int(line[2])

        graph[vex0][vex1] = weight
        if graph_type == 'U':
            graph[vex1][vex0] = weight
    
    return graph

print(adjacency_matrix("D 4\n"))

graph_string = """\
U 7
1 2
1 5
1 6
3 4
0 4
4 5
"""
pprint(adjacency_matrix(graph_string))
##graph_string = """\
##U 12 W
##0 1 1
##1 9 12
##1 10 3
##1 11 -4
##10 11 25
##"""
##
##pprint(adjacency_matrix(graph_string))



##from pprint import pprint
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
##pprint(adjacency_matrix(graph_string))
##
##from pprint import pprint
##graph_string = """\
##U 7
##1 2
##1 5
##1 6
##3 4
##0 4
##4 5
##"""
##pprint(adjacency_matrix(graph_string))
##
##graph_string = """\
##D 3
##0 1
##1 0
##0 2
##"""
##print(adjacency_matrix(graph_string))
##
##
##graph_string = """\
##D 3 W
##0 1 7
##1 0 -2
##0 2 0
##"""
##print(adjacency_matrix(graph_string))











##from pprint import pprint
##
##def adjacency_list(graph_str):
##    graph_str = graph_str.replace("\n"," ")
##    graph_str = graph_str.split(" ")
##    graph_str.pop()
##    empty_list = []
##    length = len(graph_str)
##    for i in range(int(graph_str[1])):
##        empty_list.append([])
##
##
##    if graph_str[2] == 'W':
##        j = 3
##        
##        while j <= length - 3:
##            j_E = graph_str[j + 1]
##            j_W = graph_str[j + 1 + 1]
##            
##            empty_list[int(graph_str[j])] += [(int(j_E), int(j_W))]
##            
##            if graph_str[0] == 'U':
##                empty_list[int(j_E)] += [(int(graph_str[j]), int(j_W))]
##
##            j += 3
##            j_E = 0
##            j_W = 0
##
##    else:
##        j = 2
##        
##        while j <= length - 2:
##            j_E = graph_str[j + 1]
##            empty_list[int(graph_str[j])] += [(int(j_E), None)]
##
##
##            if graph_str[0] == 'U':
##                empty_list[int(j_E)] += [(int(graph_str[j]), None)]
##                
##            j += 2
##            j_E = 0
##    return empty_list
##
##
##
##def bfs_tree(adj_list, start):
##    length = len(adj_list)
##    n = adj_list
##    state = ['U'] * length
##    parent = [None] * length
##    q = []
##    state[start] = 'D'
##    q.append(start)
##    return bfs_loop(n, q, state, parent)
##
##
##
##def bfs_loop(n, q, state, parent):
##    while q != []:
##        u = q.pop(0)
##        for v in n[u]:
##            if state[v[0]] == 'U':
##                state[v[0]] = 'D'
##                parent[v[0]] = u
##                q.append(v[0])
##        state[u] = 'P'
##        
##    return parent
##
##adj_list = [
##[(1, None)],
##[(0, None), (2, None)],
##[(1, None)]
##]
##print(bfs_tree(adj_list, 0))
##print(bfs_tree(adj_list, 1))
##
##adj_list = [
##[(1, None)],
##[]
##]
##print(bfs_tree(adj_list, 0))
##print(bfs_tree(adj_list, 1))

### graph from the textbook example
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
##print(bfs_tree(adjacency_list(graph_string), 1))

##
##graph_string = """\
##D 2 W
##0 1 99
##"""
##print(bfs_tree(adjacency_list(graph_string), 0))






##def dfs_tree(adj_list, start):
##    length = len(adj_list)
##    n = adj_list
##    state = ['U'] * length
##    parent = [None] * length
##    state[start] = 'D'
##    dfs_loop(n, start, state, parent)
##    return parent
##
##
##
##def dfs_loop(n, u, state, parent):
##    for v in n[u]:
##        if state[v[0]] == 'U':
##            state[v[0]] = 'D'
##            parent[v[0]] = u
##            dfs_loop(n, v[0], state, parent)
##
##    state[u] = 'P'
##        
##    return parent
##
# an undirected graph
##
##adj_list = [
##    [(1, None), (2, None)],
##    [(0, None), (2, None)],
##    [(0, None), (1, None)]
##]
##
##print(dfs_tree(adj_list, 0))
##print(dfs_tree(adj_list, 1))
##print(dfs_tree(adj_list, 2))
##
### a directed graph (note the asymmetrical adjacency list)
##
##adj_list = [
##[(1, None)],
##[]
##]
##
##print(dfs_tree(adj_list, 0))
##print(dfs_tree(adj_list, 1))
##
### graph from the textbook example
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
##print(dfs_tree(adjacency_list(graph_string), 1))
##
##
##gstring = """\
##U 4
##2 3
##2 1
##0 3
##1 0
##"""
##print(dfs_tree(adjacency_list(gstring), 0))
