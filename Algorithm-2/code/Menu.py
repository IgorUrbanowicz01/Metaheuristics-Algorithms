from Generator import *
from LoadingTSP import loadTSP
from Importing import *
from Calculations import tabooSearch


def menu():
    options = 0
    while options != 4:
        print("1) Load problem")
        print("2) Generate Problem")
        print("3) Show charts")
        print("4) Exit")
        options = int(input("Enter your option: "))
        if options == 1:
            distance_matrix = askUserForFilename()
            problemMenu(distance_matrix)
        if options == 2:
            distance_matrix = randMenu()
            problemMenu(distance_matrix)
        if options == 3:
            generatorMenu()
            options = 0


def randMenu():
    print("1) Symmetrical matrix")
    print("2) Non symmetrical matrix")
    print("3) wpisz swoj probelm")
    options = int(input("Enter your option: "))
    if options == 1:
        size = int(input("Enter the number of cities: "))
        min_distance = int(input("minimal distance between cities: "))
        max_distance = int(input("maximal distance between cities: "))
        seed = input("seed, You can write nothing: ")
        distancematrix = randomMatrixSym(size,min_distance, max_distance, seed)
        for i in range(0, len(distancematrix)):
            print(distancematrix[i])
        return distancematrix
    if options == 2:
        size = int(input("Enter the number of cities: "))
        min_distance = int(input("minimal distance between cities: "))
        max_distance = int(input("maximal distance between cities: "))
        seed = int(input("seed, You can write nothing: "))
        distancematrix = randomMatrixNotSym(size, min_distance, max_distance, seed)
        for i in range(0,len(distancematrix)-1):
            print(distancematrix[i])
        return distancematrix
    if options == 3:
        city = int(input("Enter the number of cities: "))
        distance_matrix = write_problem(city)
        problemMenu(distance_matrix)


def problemMenu(matrix):
    print("1) k-random")
    print("2) greedy")
    print("3) greedy expanded")
    print("4) OPT2")
    print("5) Tabu search")
    options = int(input("Enter your option: "))
    if options == 1:
        k = int(input("Enter K"))
        Path = random_alogrythm(matrix, k)
        distance = hamiltonian_path(matrix, Path)
        print("Your path is: " + str(Path))
        print("Distance for your path is: " + str(distance))
    if options == 2:
        start = int(input("Enter starting point: "))
        Path = greedy_alogrythm(matrix, start)
        distance = hamiltonian_path(matrix, Path)
        print("Your path is: " + str(Path))
        print("Distance for your path is: " + str(distance))
    if options == 3:
        Path = extended_greedy(matrix)
        distance = hamiltonian_path(matrix, Path)
        print("Your path is: " + str(Path))
        print("Distance for your path is: " + str(distance))
    if options == 4:
        Path1 = randomPermutation(len(matrix))
        Path = OPT2_alogrythm(matrix, Path1)
        distance = hamiltonian_path(matrix, Path)
        print("Your path is: " + str(Path))
        print("Distance for your path is: " + str(distance))
    if options == 5:
        length = int(input("Enter the length of the tabu array: "))
        amount = int(input("Enter the amount of iterations we stay in a neighbourhood : "))
        depth = int(input("Enter the depth of the tabu search: "))
        print("Enter the type of the tabu search: ")
        print("1) invert")
        print("2) swap")
        print("3) insert")
        print("4) revert insert")
        type = int(input("Enter a number: "))
        if type == 1:
            print(tabooSearch(matrix, length, amount, depth, "invert"))
        if type == 2:
            print(tabooSearch(matrix, length, amount, depth, "swap"))
        if type == 3:
            print(tabooSearch(matrix, length, amount, depth, "insert"))
        if type == 4:
            print(tabooSearch(matrix, length, amount, depth, "revert insert"))

def generatorMenu():
    print("1) How K effects k-random algorithm")
    print("2) Greedy vs extended greedy")
    print("3) Show PDR for all algorithms")
    print("4) How starting point effects greedy algorithm")
    print("5) Tabu size to best rout")
    print("6) Exit")
    options = int(input("Choose chart: "))
    if options == 1:
        print("Choose matrix: ")
        distance_matrix = randMenu()
        k = int(input("Enter largest K: "))
        k_random_Generator_algorythm_single_matrix(distance_matrix, k)
    if options == 2:
        city = int(input("Enter city number: "))
        greedy_vs_extended_greedy(city)
    if options == 3:
        city = int(input("Enter city number: "))
        all_alogrythm(city)
    if options == 4:
        city = int(input("Enter city number: "))
        greedy_by_n(city)
    if options == 5:
        city = int(input("Enter city number: "))
        tabu_list_size_generator(city)
    if options == 6:
        return 0

def load_TSP_menu():
    file = str(input("Enter TSP file name: "))
    distance_matrix = loadTSP(file)
    for i in range(0, len(distance_matrix)):
        print(distance_matrix[i])
    return distance_matrix