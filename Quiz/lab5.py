import math

##def adjacency_matrix(graph_str):
##    graph_str = graph_str.splitlines()
##    graph_type = graph_str[0].split()[0]
##    num_vex = int(graph_str[0].split()[1])
##
##    graph = []
##    if len(graph_str[0].split()) == 3:
##        for i in range(num_vex):
##            graph.append([None] * num_vex)
##            
##    else:
##        for i in range(num_vex):
##            graph.append([0] * num_vex)
##
##
##    for i in range(1, len(graph_str)):
##        line = graph_str[i].split()
##        weight = math.inf
##        vex0 = int(line[0])
##        vex1 = int(line[1])
##        if len(line) == 3:
##            weight = int(line[2])
##
##        graph[vex0][vex1] = weight
##        if graph_type == 'U':
##            graph[vex1][vex0] = weight
##    
##    return graph


def adjacency_list(graph_str):
##    print(graph_str)
    graph_str = graph_str.splitlines()
##    print(graph_str)
    graph_type = graph_str[0].split()[0]
##    print(graph_str[0].split())
    num_vertex = int(graph_str[0].split()[1])
    graph = [[] for i in range(num_vertex)]

    
    for i in range(1, len(graph_str)):
        line = graph_str[i].split()
##        print(line)
        weight = None
        vertex1 = int(line[0])
        vertex2 = int(line[1])
        if len(line) == 3:
            weight = int(line[2])

        graph[vertex2].append((vertex1, weight))
        if graph_type == 'U':
            graph[vertex1].append((vertex2, weight))
    
    return graph



def distance_matrix(adj_list):
    print(adj_list)
    length = len(adj_list)
    graph = []    

    for i in range(length):
        graph.append([math.inf] * length)


    for i,j in enumerate(adj_list):
        graph[i][i] = 0
        for z in j:
            vertex = int(z[0])
            distance = int(z[1])

            graph[i][vertex] = distance
##            graph[vertex][i] = distance
    
    return graph



##graph_str = """\
##U 3 W
##0 1 5
##2 1 7
##"""
##adj_list = adjacency_list(graph_str)
##print(distance_matrix(adj_list))
### more readable output (less readable code):
##print("\nEach row on a new line:")
##print("\n".join(str(lst) for lst in distance_matrix(adj_list)))
##
##
##graph_str = """\
##D 2 W
##0 1 4
##"""
##adj_list = adjacency_list(graph_str)
##print(distance_matrix(adj_list))



def floyd(distance):
##    print(distance)
    n = distance
    for k in range((len(n) - 1), -1, -1):
        for i in range(len(n) - 1, -1, -1):
            for j in range(len(n) - 1, -1, -1):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    return distance


##graph_str = """\
##D 3 W
##0 1 1
##1 2 2
##2 0 4
##"""
##adj_list = adjacency_list(graph_str)
##dist_matrix = distance_matrix(adj_list)
##print("Initial distance matrix:", dist_matrix)
##dist_matrix = floyd(dist_matrix)
##print("Shortest path distances:", dist_matrix)
##
##import pprint
##graph_str = """\
##U 7 W
##0 1 5
##0 2 7
##0 3 12
##1 2 9
##2 3 4
##1 4 7
##2 4 4
##2 5 3
##3 5 7
##4 5 2
##4 6 5
##5 6 2
##"""
##pprint.pprint(floyd(distance_matrix(adjacency_list(graph_str))))



def permutations(s):
    solutions = []
    dfs_backtrack((), s, solutions)
    return solutions


def dfs_backtrack(candidate, input_data, output_data):
    if should_prune(candidate):
        return
    if is_solution(candidate, input_data):
        add_to_output(candidate, output_data)
    else:
        for child_candidate in children(candidate, input_data):
            dfs_backtrack(child_candidate, input_data, output_data)
            
def is_solution(candidate, input_data):
    """Returns True if the candidate is complete solution"""
    return set(candidate) == set(input_data)
    # Complete the code


def children(candidate, input_data):
    """Returns a collestion of candidates that are the children of the given
    candidate."""
    child = []
##    print(candidate)
    for i in input_data:
        if i not in candidate:
##            print(candidate)
            child.append(candidate + (i,))

    return child
    # Complete the code

    
def add_to_output(candidate, output_data):
    output_data.append(candidate)

    
def should_prune(candidate):
    return False


##print(sorted(permutations({1,2,3})))
##
##print(sorted(permutations({'a'})))
##
##perms = permutations(set())
##print(len(perms) == 0 or list(perms) == [()])









def all_paths(adj_list, source, destination):
    solutions = []
    dfs_backtrack((), adj_list, solutions)
    return solutions



def dfs_backtrack(candidate, input_data, output_data):
    if should_prune(candidate):
        return
    if is_solution(candidate, input_data):
        add_to_output(candidate, output_data)
    else:
##        chosen_vertex = candidate[-1]
        for child_candidate in children(candidate, input_data):
            dfs_backtrack(child_candidate, input_data, output_data)


            
def is_solution(candidate, input_data):
    """Returns True if the candidate is complete solution"""
##    print(candidate,11)
##    print(input_data)
    return candidate == input_data
    # Complete the code



def children(candidate, input_data):
    """Returns a collestion of candidates that are the children of the given
    candidate."""
    child_candidate = []
##    print(input_data)
    for edge_pair in input_data:
        #Copy candidate tuple
##        print(edge_pair)
        adj_vertex = edge_pair[0]
        temp_path = candidate + tuple()
##        print(temp_path)
        if adj_vertex not in candidate:
            temp_path += (adj_vertex,)
            print(temp_path)
            child_candidate.append(temp_path)
            
    return child_candidate
    # Complete the code


    
def add_to_output(candidate, output_data):
    output_data.append(candidate)


    
def should_prune(candidate):
    return False


triangle_graph_str = """\
U 3
0 1
1 2
2 0
"""
adj_list = adjacency_list(triangle_graph_str)
print(sorted(all_paths(adj_list, 0, 2)))
print(all_paths(adj_list, 1, 1))



##def all_paths(adj_list, source, dest):
##    path_list = []
##    dfs_backtrack_ap((source,), adj_list, path_list, dest)
##    return path_list
##
##def dfs_backtrack_ap(path, adj_list, path_list, dest):
##    if is_solution_ap(path, dest):
##        add_to_output(path, path_list)
##    else:
##        # input_data[i] is the adj vertices for a particular vertex
##        # children to a path should be the available vertices from
##        # the last vertex in the path
##        chosen_vertex = path[-1]
##        for possible_path in children_ap(path, adj_list[chosen_vertex]):
##            dfs_backtrack_ap(possible_path, adj_list, path_list, dest)
##
##
##def is_solution_ap(path, dest):
##    """Returns True if the candidate is complete solution"""
##    # Complete the code
##    # is a solution if the last vertex in path is the destination vertex
##    return (path[-1] == dest)
##
##
##def children_ap(path, adj_vertices):
##    """Returns a collection of candidates that are the children of the given
##    candidate."""
##    possible_paths = []
##    for edge_pair in adj_vertices:
##        #Copy candidate tuple
##        adj_vertex = edge_pair[0]
##        temp_path = path + tuple()
##        if adj_vertex not in path:
##            temp_path += (adj_vertex,)
##            possible_paths.append(temp_path)
##    return possible_paths;
##    # Complete the code
##
##def add_to_output(candidate, output_data):
##    output_data.append(candidate)
