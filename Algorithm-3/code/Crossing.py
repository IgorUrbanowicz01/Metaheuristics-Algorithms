import random
from Misc_functions import calculateDistance


def getIndex(a, arr):
    for i in range(len(arr)):
        if a == arr[i]:
            return i
    
    return -1


def mapElements(a1, a2, a3, b1, b2, b3):
    for i in range(len(a1)):
        if a1[i] in a2:
            curr = getIndex(a1[i], a2)
            while getIndex(b2[curr], a2) != -1:
                curr = getIndex(b2[curr], a2)
            a1[i] = b2[curr]
    
    for i in range(len(a3)):
        if a3[i] in a2:
            curr = getIndex(a3[i], a2)
            while getIndex(b2[curr], a2) != -1:
                curr = getIndex(b2[curr], a2)
            a3[i] = b2[curr]
    
    for i in range(len(b1)):
        if b1[i] in b2:
            curr = getIndex(b1[i], b2)
            while getIndex(a2[curr], b2) != -1:
                curr = getIndex(a2[curr], b2)
            b1[i] = a2[curr]
    
    for i in range(len(b3)):
        if b3[i] in b2:
            curr = getIndex(b3[i], b2)
            while getIndex(a2[curr], b2) != -1:
                curr = getIndex(a2[curr], b2)
            b3[i] = a2[curr]


def fillMiddle(a1, a2, a3, b1, b2, b3):
    a_base = a1 + a2 + a3
    b_base = b1 + b2 + b3
    b = b_base.copy()
    
    for x in a1 + a3:
        b.remove(x)
    a2 = b.copy()
    
    a = a_base.copy()
    
    for y in b1 + b3:
        a.remove(y)
    b2 = a.copy()
    
    new_a = a1 + a2 + a3
    new_b = b1 + b2 + b3
    return [new_a, new_b]


def crossPMX(arr1, arr2):
    point1 = random.randint(1, len(arr1) - 3)
    point2 = random.randint(point1 + 1, len(arr1) - 1)
    
    a1 = arr1[:point1]
    a2 = arr1[point1:point2]
    a3 = arr1[point2:]
    
    b1 = arr2[:point1]
    b2 = arr2[point1:point2]
    b3 = arr2[point2:]
    
    mapElements(a1, b2, a3, b1, a2, b3)
    
    return [a1 + b2 + a3, b1 + a2 + b3]


def crossOX(arr1, arr2):
    point1 = random.randint(0, len(arr1) - 2)
    point2 = random.randint(point1 + 1, len(arr1) - 1)
    
    a1 = arr1[:point1]
    a2 = arr1[point1:point2]
    a3 = arr1[point2:]
    
    b1 = arr2[:point1]
    b2 = arr2[point1:point2]
    b3 = arr2[point2:]
    
    children = fillMiddle(a1, a2, a3, b1, b2, b3)
    child1 = children[0]
    child2 = children[1]
    
    return [child1, child2]


def crossPopulation(distance_matrix, population, probability, cross_function):
    newPopulation = population.copy()
    crossNum = len(population) // 2
    
    for i in range(0, crossNum):
        
        roll = random.randint(0, 100)
        if roll < probability:
            parent1 = population[2 * i][0]
            parent2 = population[2 * i + 1][0]
            children = cross_function(parent1, parent2)
            child1 = [children[0], calculateDistance(children[0], distance_matrix), 0]
            child2 = [children[1], calculateDistance(children[1], distance_matrix), 0]
            newPopulation.append(child1)
            newPopulation.append(child2)
    
    return newPopulation
