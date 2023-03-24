import random

from TPS_functions import *


def randomMatrixSym(size, min_range, max_range, seed=None):
    matrix = []

    random.seed(seed)

    for i in range(0, size):
        matrix.append([])
        for j in range(0, i):
            matrix[i].append(random.randint(min_range, max_range))
        matrix[i].append(-1)


    return triangleToSquareMatrix(matrix)


def randomMatrixNotSym(size, min_range, max_range, seed=None):
    matrix = []

    random.seed(seed)
    for i in range(0, size):
        matrix.append([])
        for k in range(0, i):
            matrix[i].append(random.randint(min_range, max_range))
        matrix[i].append(-1)
        for j in range(i + 1, size):
            matrix[i].append(random.randint(min_range, max_range))

    return matrix


def pints_to_matrixTSP(file):
    G = file.get_graph()
    Coordinates = []
    for i in range(1, len(G.nodes)+1):  # Saves coordinate to coordinate list
        x, y = file.node_coords[i]
        Coordinates.append([float(x), float(y)])

    return triangleToSquareMatrix(pointsToMatrix(Coordinates))


def pointsToMatrix(points):
    matrix = []
    for i in range(len(points)):
        row = []
        for j in range(0, i + 1):
            if i != j:
                distance_ = distance(int(points[i][0]),
                                             int(points[i][1]),
                                             int(points[j][0]),
                                             int(points[j][1]))
                row.append(distance_)
            else:
                row.append(-1)
        matrix.append(row)

    return matrix

def triangleToSquareMatrix(matrix):

    newMatrix = matrix

    size = len(matrix)

    if len(matrix[0]) == size:
        for i in range(size):
            for j in range(0, i):
                newMatrix[i].append(matrix[j][i])
        return newMatrix
    else:
        for i in range(size):
            for j in range(i+1, size):
                newMatrix[i].append(matrix[j][i])
        return newMatrix

def wierdtriangleToSquareMatrix(problem):
    distance_matrix = problem.edge_weights
    new_distance_matrix = []
    k = 0
    w = 0
    for i in range(0, len(list(problem.get_nodes()))):
        new_distance_matrix.append([])
        for j in range(0, i+1):
            if callable(distance_matrix[k][w]):
                print(k, end= " ")
                print(w)
                end = 1
                break
            new_distance_matrix[i].append(distance_matrix[k][w])
            w += 1
            # print(k, end= " ")
            # print(w)
            if w == len(distance_matrix[k])-1:
                w = 0
                k += 1
        print(new_distance_matrix[i])
    if end == 1:
        return triangleToSquareMatrix(new_distance_matrix)
    return triangleToSquareMatrix(new_distance_matrix)