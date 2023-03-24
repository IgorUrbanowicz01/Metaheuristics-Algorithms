from Matrix_funcions import triangleToSquareMatrix
from TPS_functions import *


def greedy_alogrythm(data, starting_point):
    currNode = starting_point
    permutation = [currNode]

    possible = list(range(len(data)))
    for i in range(len(data) - 1):
        possible.remove(currNode)

        possibleNext = []
        for p in possible:
            possibleNext.append(data[currNode][p])

        minimalIndex = possible[0]
        minimal = possibleNext[0]
        for m in range(len(possibleNext)):
            if possibleNext[m] < minimal:
                minimal = possibleNext[m]
                minimalIndex = possible[m]

        currNode = minimalIndex
        permutation.append(currNode)

    return permutation


def extended_greedy(data):
    bestDistance = -1
    bestPermutation = []

    for s in range(len(data)):
        permutation = greedy_alogrythm(data, s)
        dist = hamiltonian_path(data, permutation)

        if s == 0 or dist < bestDistance:
            bestDistance = dist
            bestPermutation = permutation

    return bestPermutation
