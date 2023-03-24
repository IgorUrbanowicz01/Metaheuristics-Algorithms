import random

from Greedy_algorythm import greedy_algorithm
from Misc_functions import generateRandomPermutation, calculateDistance


def initial_select(distance_matrix, paths_amount, elite_percent):
    # paths_amount - amount of initial paths,
    # elite_percent - Percentage of paths made by greedy algorythm
    initial_paths = []
    elites = round(paths_amount * elite_percent / 100)
    for i in range(elites):
        permutation = greedy_algorithm(distance_matrix, i % len(distance_matrix))
        permutation_length = calculateDistance(permutation, distance_matrix)
        initial_paths.append([permutation, permutation_length, 0])
    for i in range(paths_amount - elites):
        permutation = generateRandomPermutation(len(distance_matrix))
        permutation_length = calculateDistance(permutation, distance_matrix)
        initial_paths.append([permutation, permutation_length, 2])

    return initial_paths


def find_tournament_winner(tournament):
    bestDistance = tournament[0][1]
    final_path = tournament[0]
    for path in tournament:
        if path[1] < bestDistance:
            bestDistance = path[1]
            final_path = path
    return final_path


def select(select_size, paths, type):
    
    if type == "TUR":
        tournament_winners = []
        for i in range(len(paths)):
            tournament = []
            for j in range(select_size):
                tournament.append(random.choice(paths))
            tournament_winners.append(find_tournament_winner(tournament))
        # print(tournament_winners)
        return tournament_winners
    else:
        if type == "PRB":
            sum = 0
            probability = []
            probability_test = []
            tournament_winners = []
            probability.append(0)
            for i in range(0, len(paths)):
                sum += paths[i][1]
            for i in range(1, len(paths)):
                probability.append(sum/paths[i][1]+probability[i-1])
                probability_test.append(paths[i][1])
            for i in range(select_size):
                random_path = random.randint(0, int(probability[len(paths)-1]))
                for j in range(0, len(paths)):
                    if probability[j] > random_path:
                        # print(random_path)
                        # print(paths[j])
                        tournament_winners.append(paths[j])
                        break


            # print(probabilitytest)
            # print(probability)
            # print(tournament_winners)

