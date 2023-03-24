import random
from Misc_functions import calculateDistance


def swapRandom(permutation):
    i = random.randint(0, len(permutation) - 1)
    j = random.randint(0, len(permutation) - 1)
    while i == j:
        j = random.randint(0, len(permutation) - 1)
        
    permutation[i], permutation[j] = permutation[j], permutation[i]


def mutate(permutation, probability):
    if probability >= 100:
        return
    roll = random.randint(0, 100)
    mutated = False
    while roll < probability:
        mutated = True
        swapRandom(permutation)
        roll = random.randint(0, 100)
    return [permutation, mutated]
        

def mutatePopulation(distance_matrix, population, probability):
    
    newPopulation = []
    
    for specimen in population:
    
        mutation_result = mutate(specimen[0], probability)
        mutated = mutation_result[1]
        
        if mutated:
            permutation = mutation_result[0]
            age = specimen[2]
            length = calculateDistance(permutation, distance_matrix)
            newSpecimen = [permutation, length, age]
        else:
            newSpecimen = specimen.copy()
            
        newPopulation.append(newSpecimen)
    
    return newPopulation

