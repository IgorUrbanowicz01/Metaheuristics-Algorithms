import tsplib95
import networkx as nx
import re


def askUserForFilename():
    file_name = input("Podaj nazwę pliku\n")
    data_matrix = tsplib95.load('Problems/' + file_name)
    distance_matrix = get_distance_matrix(data_matrix)
    # print(distance_matrix)
    return distance_matrix


def getNumbersFromString(string):
    new_array = []
    next_number = -1
    for c in string:
        if c.isdigit():
            if next_number == -1:
                next_number = 0
            next_number = next_number*10 + int(c)
        else:
            if next_number != -1:
                new_array.append(next_number)
                next_number = -1
    return new_array


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

def write_problem(city_count):
    problem = []

    for i in range(city_count):
        row = []
        for j in range(city_count):
            row.append(0)
        problem.append(row)



    for i in range(city_count):
        for j in range(city_count):
            if i != j:
                print('Podaj odległośc z miasta', i, 'do', j)
                problem[i][j] = int(input())

    return problem