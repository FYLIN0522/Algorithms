##==== Question 1 Converters ============================================================
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
            if state[v] == 'U':
                state[v] = 'D'
                parent[v] = u
                q.append(v)
        state[u] = 'P'
        
    return parent


def treepath(parent, s, t):
    if s == t:
        return [s]
    else:
        return [t] + treepath(parent, s, parent[t])


def format_sequence(converters_info, source_format, destination_format):
    converters_info = converters_info.replace("\n"," ")
    converters_info = converters_info.split(" ")
    converters_info.pop()
    res_list = []
    length = len(converters_info)
    found = False
    res = []
    
    for i in range(int(converters_info[1])):
        res_list.append([])
        

    j = 2 
    while j <= length - 2:
        j_E = converters_info[j + 1]
        res_list[int(converters_info[j])] += [int(j_E)]
        
        if destination_format == int(j_E):
            found = True
            index = int(converters_info[j])
        
        j += 2
        j_E = 0
    
    if source_format == destination_format:
        return [destination_format]

    elif destination_format in res_list[source_format]:
        return[source_format, destination_format] 

    elif found:
        parent = bfs_tree(res_list, source_format)
        res += treepath(parent, source_format, destination_format)
        res = res[::-1]
        
    else:
        return "No solution!"

    
    return res

#### Testing
####[1, 3, 0]
####True
####[4]
####[3]
####[3, 0, 2]
####No solution!
##
##converters_info_str = """\
##D 2
##0 1
##"""
##source_format = 0
##destination_format = 1
##print(format_sequence(converters_info_str, source_format, destination_format))
##
##
##converters_info_str = """\
##D 2
##0 1
##"""
##print(format_sequence(converters_info_str, 1, 1))
##
##
##
##converters_info_str = """\
##D 2
##0 1
##"""
##print(format_sequence(converters_info_str, 1, 0))
##
##
##
##converters_info_str = """\
##D 5
##1 0
##0 2
##2 3
##1 2
##"""
##print(format_sequence(converters_info_str, 1, 2))
##
##
##
##converters_info_str = """\
##D 1
##"""
##print(format_sequence(converters_info_str, 0, 0))
##
##
##
##
##converters_info_str = """\
##D 5
##0 1
##0 2
##1 2
##2 3
##1 3
##3 0
##"""
##
##print(format_sequence(converters_info_str, 1, 0))
##print(format_sequence(converters_info_str, 0, 3) in [[0, 1, 3], [0, 2, 3]])
##print(format_sequence(converters_info_str, 4, 4))
##print(format_sequence(converters_info_str, 3, 3))
##print(format_sequence(converters_info_str, 3, 2))
##print(format_sequence(converters_info_str, 3, 4))
















##==== Question 2 Bubbles ===========================================================
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
            if state[v] == 'U':
                state[v] = 'D'
                parent[v] = u
                q.append(v)
        state[u] = 'P'
        
    return parent



def connected_components(adj):
    length = len(adj)
    n = adj
    state = ['U'] * length
    parent = [None] * length
    q = []
    components = []

    
    for i in range(len(n)):
##    while 'U' in state:
        if state[i] == 'U':
            previous_state = state.copy()
            state[i] == 'D'
            q.append(i)
            bfs_loop(adj, q, state, parent)

        if previous_state != state:
            components.append([])
            
            for j in range(len(previous_state)):
                if previous_state[j] != state[j]:          
                    components[-1] += [j]
                    
            previous_state = state
    return components



def bubbles(physical_contact_info):
    physical_contact_info = physical_contact_info.replace("\n"," ")
    physical_contact_info = physical_contact_info.split(" ")
    physical_contact_info.pop()
    res_list = []
    length = len(physical_contact_info)
    for i in range(int(physical_contact_info[1])):
        res_list.append([])


    j = 2
    while j <= length - 2:
        j_E = physical_contact_info[j + 1]
        res_list[int(physical_contact_info[j])] += [int(j_E)]
        res_list[int(j_E)] += [int(physical_contact_info[j])]
##        print(int(physical_contact_info[j]), int(j_E))
                                               
        j += 2
        j_E = 0


    res = connected_components(res_list)

    return res


#### Testing
##physical_contact_info = """\
##U 2
##0 1
##"""
##print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))
##
##
##physical_contact_info = """\
##U 2
##"""
##print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))
##
##
##physical_contact_info = """\
##U 7
##1 2
##1 5
##1 6
##2 3
##2 5
##3 4
##4 5
##"""
##print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))
##
##
##physical_contact_info = """\
##U 0
##"""
##print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))
##
##
##physical_contact_info = """\
##U 1
##"""
##print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))
##
##
##physical_contact_info = """\
##U 7
##1 4
##2 0
##4 6
##5 3
##"""
##print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))











####==== Question 3 Package management ===========================================================
def dfs_tree(adj_list, start):
    length = len(adj_list)
    n = adj_list
    state = ['U'] * length
    parent = [None] * length
    state[start] = 'D'
    stack = []
    
    for i in range(length):
        dfs_loop(n, i, state, parent, stack)
        
    return stack



def dfs_loop(n, u, state, parent, stack):
##    if u not in stack:
##        stack.insert(0, u)
    for v in n[u]:
        if state[v] == 'U':
            state[v] = 'D'
            parent[v] = u

            
            dfs_loop(n, v, state, parent, stack)
            
        state[u] = 'P'
        
    if u not in stack:
        stack.insert(0, u)


            
def build_order(dependencies):
    dependencies = dependencies.replace("\n"," ")
    dependencies = dependencies.split(" ")
    dependencies.pop()
    res_list = []
    length = len(dependencies)

    for i in range(int(dependencies[1])):
        res_list.append([])
        
    j = 2 
    while j <= length - 2:
        j_E = dependencies[j + 1]
        res_list[int(dependencies[j])] += [int(j_E)]
        
        j += 2
        j_E = 0


    res = dfs_tree(res_list, 0)

    
    return res
#### Testing
##dependencies = """\
##D 6
##0 2
##1 2
##1 0
##4 1
##4 0
##4 5
##2 3
##3 5
##"""
##
##print(build_order(dependencies))

##dependencies = """\
##D 7
##0 3
##4 0
##5 3
##3 2
##4 5
##
##"""
##
##print(build_order(dependencies))
##dependencies = """\
##D 2
##0 1
##"""
##
##print(build_order(dependencies))
##
##dependencies = """\
##D 3
##1 2
##0 2
##"""
##
##print(build_order(dependencies) in [[0, 1, 2], [1, 0, 2]])
##
##dependencies = """\
##D 3
##"""
### any permutation of 0, 1, 2 is valid in this case.
##solution = build_order(dependencies)
##if solution is None:
##    print("Wrong answer!")
##else:
##    print(sorted(solution))













####===== Question 4 Snow ===========================================================
def next_vertex(in_tree, distance):
    v_list = [] 
    next_vertex = None
    
    for index, vertex in enumerate(in_tree): 
        if not vertex:
            v_list.append(index)
     
    min_weight = distance[v_list[0]] 
    next_vertex = v_list[0]
    
    for i in v_list: 
        temp_weight = distance[i] 
        if temp_weight < min_weight: 
            min_weight = temp_weight
            next_vertex = i
            
    return next_vertex



def prim(adj_list, start):
    n = adj_list
    in_tree = [False] * len(adj_list)
    distance = [float('inf')] * len(adj_list)
    parent = [None] * len(adj_list)
    distance[start] = 0

    
    while False in in_tree:
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        
        for v, weight in n[u]:
            if in_tree[v] is False and weight < distance[v]:
                distance[v] = weight
                parent[v] = u
            
                 
    return parent


    
def which_segments(city_map):
    city_map = city_map.replace("\n"," ")
    city_map = city_map.split(" ")
    city_map.pop()
    res_list = []
    length = len(city_map)

    for i in range(int(city_map[1])):
        res_list.append([])
    

    j = 3
    
    while j <= length - 3:
        j_E = city_map[j + 1]
        j_W = city_map[j + 1 + 1]
        
        res_list[int(city_map[j])] += [(int(j_E), int(j_W))]
        res_list[int(j_E)] += [(int(city_map[j]), int(j_W))]

        j += 3
        j_E = 0
        j_W = 0

    parent = prim(res_list, 0)
##    print(parent)
    res = []
    index = 1
    for z in parent[1:]:
##        print(z)
        res.append((min(z, index), max(z, index)))
        index += 1
        
    return res

#### Testing
##city_map = """\
##U 3 W
##0 1 1
##2 1 2
##2 0 4
##"""
##print(sorted(which_segments(city_map)))
##
##[(0, 3), (1, 2), (2, 3)]
##city_map = """\
##U 4 W
##0 1 5
##1 3 5
##3 2 3
##2 0 5
##0 3 2
##1 2 1
##"""
##
##print(sorted(which_segments(city_map)))
##
##city_map = """\
##U 3 W
##0 1 1
##2 1 2
##2 0 4
##"""
##print(sorted(which_segments(city_map)))
##
##
##city_map = """\
##U 1 W
##"""
##print(sorted(which_segments(city_map)))













##==== Question 5 Batteries ============================================================
import math
def next_vertex(in_tree, distance):
    v_list = [] 
    next_vertex = None
    
    for index, vertex in enumerate(in_tree): 
        if not vertex:
            v_list.append(index)
            
    min_weight = distance[v_list[0]] 
    next_vertex = v_list[0]
    
    for i in v_list: 
        temp_weight = distance[i] 
        if temp_weight < min_weight: 
            min_weight = temp_weight
            next_vertex = i
            
    return next_vertex



def Dijkstra(adj_list, start):
    n = adj_list
    in_tree = [False] * len(adj_list)
    distance = [float('inf')] * len(adj_list)
    parent = [None] * len(adj_list)
    distance[start] = 0

    
    while False in in_tree:
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        
        for v, weight in n[u]:
            if in_tree[v] is False and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                parent[v] = u
            
                 
    return distance



def min_capacity(city_map, depot_position):
    city_map = city_map.replace("\n"," ")
    city_map = city_map.split(" ")
    city_map.pop()
    res_list = []
    length = len(city_map)
    
    for i in range(int(city_map[1])):
        res_list.append([])


    j = 3
    while j <= length - 3:
        j_E = city_map[j + 1]
        j_W = city_map[j + 1 + 1]
        
        res_list[int(city_map[j])] += [(int(j_E), int(j_W))]
        
        res_list[int(j_E)] += [(int(city_map[j]), int(j_W))]

        j += 3
        j_E = 0
        j_W = 0

    res = Dijkstra(res_list, depot_position)
##    print(res)
    max_distance = 0
    for z in res:
        if z != float('inf') and z > max_distance:
            max_distance = z

##    print(max_distance) 
    res_num = int(math.ceil(max_distance * 3 / 0.75))
    
    return res_num


##1400
##1400
##800

##city_map = """\
##U 3 W
##0 1 3
##0 2 5
##"""
##
##print(min_capacity(city_map, 0))
##print(min_capacity(city_map, 1))
##print(min_capacity(city_map, 2))
##
##city_map = """\
##U 7 W
##0 1 6
##1 2 6
##0 2 10
##0 3 3
##3 4 3
##4 5 1
##"""
##
##print(min_capacity(city_map, 0))
##print(min_capacity(city_map, 1))
##print(min_capacity(city_map, 2))
##print(min_capacity(city_map, 3))
##print(min_capacity(city_map, 4))
##print(min_capacity(city_map, 5))
##print(min_capacity(city_map, 6))
##
##city_map = """\
##U 4 W
##0 2 5
##0 3 2
##3 2 2
##"""
##print(min_capacity(city_map, 0))
##print(min_capacity(city_map, 1))
##print(min_capacity(city_map, 2))
##print(min_capacity(city_map, 3))
##
##
##	
##city_map = """\
##U 1000 W
##810 820 100
##830 840 100
##810 830 100
##820 840 200
##810 840 500
##840 850 100
##860 850 100
##860 840 150
##880 870 100
##890 880 100
##"""
##
##print(min_capacity(city_map, 810))
##print(min_capacity(city_map, 820))
##print(min_capacity(city_map, 890))



