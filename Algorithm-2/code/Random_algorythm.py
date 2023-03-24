import random
from TPS_functions import *

def random_alogrythm(data, k):
    random.seed()
    bestRaut = randomPermutation(len(data))
    concurrentRout = bestRaut.copy()
    for i in range(k):
        random.shuffle(concurrentRout)
        if hamiltonian_path(data, concurrentRout) < hamiltonian_path(data, bestRaut):
            bestRaut = concurrentRout.copy()
    return bestRaut