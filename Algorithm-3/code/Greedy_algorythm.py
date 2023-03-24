from Misc_functions import calculateDistance


def greedy_algorithm(data, starting_point):
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


def extended_greedy(distance_matrix):
    bestDistance = -1
    bestPermutation = []

    for s in range(len(distance_matrix)):
        permutation = greedy_algorithm(distance_matrix, s)
        dist = calculateDistance(distance_matrix, permutation)

        if s == 0 or dist < bestDistance:
            bestDistance = dist
            bestPermutation = permutation

    return bestPermutation
