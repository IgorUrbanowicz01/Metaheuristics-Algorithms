import random

from Random_algorythm import random_alogrythm
from Greedy_algorythm import *
from OPT2_algorythm import OPT2_alogrythm
from Charts import *
from TPS_functions import *
from Matrix_funcions import *
import timeit



def k_random_Generator_algorythm_single_matrix(distanceMatrix, maxk):
    resoult = []
    ktable = []
    distance = 0
    k = len(distanceMatrix)
    while k < maxk:
        for i in range(1, 50):
            Path = random_alogrythm(distanceMatrix, k)
            distance += hamiltonian_path(distanceMatrix, Path)
        distance = distance / 50
        resoult.append(round(distance, 2))
        ktable.append(k)
        print(k)
        k = k + len(distanceMatrix)
    create_chart(ktable, resoult, "k-sort" ,'numbers of randomly picked paths [k]', 'best path for k-sort algorythm avg of 50',
                 'Best path for random matrix size ' + str(len(distanceMatrix)))

    Path1 = randomPermutation(len(distanceMatrix))
    Path = OPT2_alogrythm(distanceMatrix, Path1)
    distance = hamiltonian_path(distanceMatrix, Path)
    add_line(distance, ktable, "OPT2")
    Path = greedy_alogrythm(distanceMatrix, 1)
    distance = hamiltonian_path(distanceMatrix, Path)
    print(Path)
    print(hamiltonian_path(distanceMatrix, Path))
    add_line(distance, ktable, "Greedy")
    show_chart()


def greedy_vs_extended_greedy(city_count):
    greedy_result_table = []
    extended_greedy_result_table = []
    ichart = []
    greedy_result = 0
    extended_greedy_result = 0
    i= 50
    while i < city_count:
        for k in range(1, 12):
            distanceMatrix = randomMatrixSym(i, 0, 100)
            Path = greedy_alogrythm(distanceMatrix, 0)
            greedy_result = greedy_result + hamiltonian_path(distanceMatrix, Path)
            Path = extended_greedy(distanceMatrix)
            extended_greedy_result = extended_greedy_result + hamiltonian_path(distanceMatrix, Path)
        print(i)
        greedy_result_table.append(greedy_result/12)
        extended_greedy_result_table.append(extended_greedy_result/12)
        ichart.append(i)
        i += 10

    create_chart(ichart, greedy_result_table,'greed')
    create_chart(ichart, extended_greedy_result_table, 'extended greed' ,"Number of cities", "Best path (AVG 25)", "Best paths for "
                                                                                                 "random matrixes by "
                                                                                                 "number of cities")
    show_chart()

def all_alogrythm(city_count):
    extended_greedy_result_table = []
    # extended_greedy_time_table = []
    randomk_result_table = []
    # randomk_time_table = []
    OPT2_result_table = []
    # OPT2_time_table = []
    ichart = []
    extended_greedy_result = 0; randomk_result = 0; OPT2_result = 0
    # extended_greedy_time = 0; randomk_time= 0; OPT2_time = 0
    i = 10
    while i <= city_count:
        for k in range(1, 10):
            distanceMatrix = randomMatrixSym(i, 0, 100)
            # start1 = timeit.timeit()
            Path = extended_greedy(distanceMatrix)
            # end1 = timeit.timeit()
            extended_greedy_result += hamiltonian_path(distanceMatrix, Path)
            # extended_greedy_time += start1-end1

            Path1 = randomPermutation(len(distanceMatrix))
            # start2 = timeit.timeit()
            Path = OPT2_alogrythm(distanceMatrix, Path1)
            # end2 = timeit.timeit()
            OPT2_result += hamiltonian_path(distanceMatrix, Path)
            # OPT2_time += start2 - end2

            # start3 = timeit.timeit()
            Path = random_alogrythm(distanceMatrix, i*i*i)
            # end3 = timeit.timeit()
            randomk_result += hamiltonian_path(distanceMatrix, Path)
            # randomk_time += start3 - end3

        extended_greedy_result_table.append(extended_greedy_result/10)
        # extended_greedy_time_table.append(extended_greedy_time/10)
        randomk_result_table.append(randomk_result/10)
        # randomk_time_table.append(randomk_time/10)
        OPT2_result_table.append(OPT2_result/10)
        # OPT2_time_table.append(OPT2_time/10)
        ichart.append(i)
        print(i)
        i += 10

    create_all_chart(ichart, extended_greedy_result_table, randomk_result_table, OPT2_result_table,"extended greedy","random k = city^2","2OPT","cities",'best path (AVG 10)', 'best path for each algorythm')

    for i in range(len(ichart)):
        base = min(extended_greedy_result_table[i], randomk_result_table[i], OPT2_result_table[i])
        extended_greedy_result_table[i] = PRD(base, extended_greedy_result_table[i])
        randomk_result_table[i] = PRD(base, randomk_result_table[i])
        OPT2_result_table[i] = PRD(base, OPT2_result_table[i])

    clear_chart()
    create_all_chart(ichart, extended_greedy_result_table, randomk_result_table, OPT2_result_table,"extended greedy","random k = city^3","2OPT", "cities", "PRD", "PRD for each algorythm")
    clear_chart()
    create_chart(ichart, extended_greedy_result_table, "greedy")
    create_chart(ichart, OPT2_result_table, "OPT2", "cities", "PRD", "PRD for each algorythm")
    show_chart()


def greedy_by_n(city_count):
    final = 0
    greedy_result_table = []
    greedy_result_table_PRD = []
    ichart = [i for i in range(city_count-1)]
    distanceMatrix = randomMatrixSym(city_count, 0, 100)
    for i in range(city_count-1):
        Path = greedy_alogrythm(distanceMatrix, i)
        distance = hamiltonian_path(distanceMatrix, Path)
        greedy_result_table.append(distance)
    greedy_result_table.sort()
    print("PRD for this city is:", end=" ")
    print(PRD(greedy_result_table[0], greedy_result_table[len(greedy_result_table)-1]))
    create_chart(ichart, greedy_result_table, "greedy", "Best to worst city", "Best Path", "How starting city "
                                                                                                "effects greedy "
                                                                                                "algorithm")
    show_chart()
    for j in range(1, 100):
        for i in range(city_count - 1):
            distanceMatrix = randomMatrixSym(city_count, 0, 100)
            Path = greedy_alogrythm(distanceMatrix, i)
            distance = hamiltonian_path(distanceMatrix, Path)
            greedy_result_table_PRD.append(distance)
        greedy_result_table_PRD.sort()
        final += PRD(greedy_result_table_PRD[0], greedy_result_table_PRD[len(greedy_result_table_PRD)-1])
        greedy_result_table_PRD.clear()
    print("Average PRD for worst/best city is: ", end="")
    print(final/140)