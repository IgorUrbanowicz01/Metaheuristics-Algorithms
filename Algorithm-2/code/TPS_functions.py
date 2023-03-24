import math
import random


def hamiltonian_path(Matrix, path):
    sum = 0
    for i in range(len(path)):
        sum += Matrix[path[i]][path[(i + 1) % len(path)]]
    return sum


def distance(x1, y1, x2, y2):  # Returns the distance between two points
    return int(round(math.sqrt((float(x1) - float(x2)) ** 2 + (float(y1) - float(y2)) ** 2)))


def randomPermutation(size):
    permutation = []

    while len(permutation) < size:
        r = random.randint(0, size - 1)
        if permutation.count(r) == 0:
            permutation.append(r)

    return permutation


def PRD(base, compare):
    return (compare - base) / base
