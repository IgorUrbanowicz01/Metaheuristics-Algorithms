import random


def getAge(pop):
    return pop[2]


def killTheOld(population, max_pop):
    population.sort(key=getAge)
    newPop = population[:max_pop]
    random.shuffle(newPop)
    return newPop


