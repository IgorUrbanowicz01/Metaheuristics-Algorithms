import tsplib95


def askUserForFilename():
    file_name = input("Podaj nazwę pliku\n")
    data_matrix = tsplib95.load('Problems/' + file_name)
    distance_matrix = get_distance_matrix(data_matrix)
    # print(distance_matrix)
    return distance_matrix


def get_distance_matrix(problem):

    distance_matrix = []
    index = 0
    for i in list(problem.get_nodes()):
        distance_matrix.append([])
        for j in list(problem.get_nodes()):
            # print(str(i) + "    " + str(j))
            edge = i, j
            distance_matrix[index].append(problem.get_weight(*edge))
        index += 1
    print(distance_matrix)
    return distance_matrix
