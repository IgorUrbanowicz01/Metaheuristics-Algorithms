import tsplib95
from Matrix_funcions import *

def loadTSP(file):
    problem = tsplib95.load(file)
    distance_matrix = problem.edge_weights
    if distance_matrix == []:
        return pints_to_matrixTSP(problem)
    elif problem.is_full_matrix():
        return distance_matrix
    elif len(distance_matrix[int(len(distance_matrix)/2)]) == len(distance_matrix):
        return distance_matrix
    elif len(distance_matrix[0]) == 1 or len(distance_matrix[len(distance_matrix)-1]) == 1:
        distance_matrix = problem.edge_weights
        return triangleToSquareMatrix(distance_matrix)
    else:
        return wierdtriangleToSquareMatrix(problem)