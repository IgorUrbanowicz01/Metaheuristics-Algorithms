from Select import initial_select
from Select import select
from Crossing import crossPopulation, crossOX, crossPMX
from Mutating import mutatePopulation
from Misc_functions import getBestSpecimen
from Aging import killTheOld


def geneticAlgorithm(distance_matrix, amount_of_paths, elite_percent, loops,  # Initial
                     select_type, tournament_size, max_population,            # Select
                     crossing_chance, crossing_function,                      # Crossing
                     mutation_chance):                                        # Mutation
     
    # Starting population
    population = initial_select(distance_matrix, amount_of_paths, elite_percent)

    # For stop condition
    for loop in range(loops):
        print('loop', loop)
        
        # Select
        population = select(tournament_size, population, select_type)
        
        # Age
        population = killTheOld(population, max_population)
    
        # Crossing
        population = crossPopulation(distance_matrix, population, crossing_chance, crossing_function)
        
        # Mutation
        population = mutatePopulation(distance_matrix, population, mutation_chance)

        print('Pop count:', len(population))
    best = getBestSpecimen(population)
    print('Best permutation:', best[0])
    print('Best length:', best[1])
    return population


geneticAlgorithm([[1, 2, 3, 4], [8, 12, 45, 3], [6, 34, 12, 10], [7, 32, 13, 1]], 100, 10, 100, "TUR", 10, 1000, 80,
                 crossPMX, 10)

