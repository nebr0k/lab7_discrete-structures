import numpy as np



def create_adjacency_matrix(filename):
    with open(filename, 'r') as f:
        n, m = map(int, f.readline().split())
        adjacency_matrix = np.zeros((n, n), dtype=int)
        for i in range(m):
            u, v = map(int, f.readline().split())
            adjacency_matrix[u-1][v-1] = 1
    return adjacency_matrix



def calculate_degree(adjacency_matrix):
    in_degree = np.sum(adjacency_matrix, axis=0)
    out_degree = np.sum(adjacency_matrix, axis=1)
    return in_degree, out_degree



def find_isolated_pendant_vertices(adjacency_matrix):
    n = len(adjacency_matrix)
    isolated_vertices = []
    pendant_vertices = []
    for i in range(n):
        if np.sum(adjacency_matrix[i]) == 0:
            isolated_vertices.append(i)
        elif np.sum(adjacency_matrix[i]) == 1:
            pendant_vertices.append(i)
    return isolated_vertices, pendant_vertices



def is_homogeneous(adjacency_matrix):
    in_degree, out_degree = calculate_degree(adjacency_matrix)
    if np.all(in_degree == out_degree):
        return True
    else:
        return False



def calculate_homogeneity_degree(adjacency_matrix):
    if is_homogeneous(adjacency_matrix):
        in_degree, out_degree = calculate_degree(adjacency_matrix)
        return np.sum(in_degree) / len(in_degree)
    else:
        return None



def print_degree(adjacency_matrix):
    in_degree, out_degree = calculate_degree(adjacency_matrix)
    print("In-Degree: ", in_degree)
    print("Out-Degree: ", out_degree)



def print_isolated_pendant_vertices(adjacency_matrix):
    isolated_vertices, pendant_vertices = find_isolated_pendant_vertices(adjacency_matrix)
    print("Isolated vertices: ", isolated_vertices)
    print("Pendant vertices: ", pendant_vertices)



if __name__ == '__main__':

    filename = input("Enter the input filename: ")
    adjacency_matrix = create_adjacency_matrix(filename)


    print_degree(adjacency_matrix)


    if is_homogeneous(adjacency_matrix):

        print("The graph is not homogeneous.")
    else:
        homogeneity_degree = calculate_homogeneity_degree(adjacency_matrix)
        print("The graph is homogeneous with a degree of homogeneity of ", homogeneity_degree)


    print_isolated_pendant_vertices(adjacency_matrix)
