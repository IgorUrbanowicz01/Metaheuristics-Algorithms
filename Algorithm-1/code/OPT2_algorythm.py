from TPS_functions import hamiltonian_path


def OPT2_swap(path, i, k):
    newpath = path.copy()
    z = 0
    for x in range(i, k + 1):
        newpath[i + z] = (path[k - z])
        z += 1
    return newpath


def OPT2_swap2(rout, i, k):
    while i < k:
        rout[i], rout[k] = rout[k], rout[i]
        i += 1
        k -= 1


def OPT2_alogrythm(Matrix, path_to_enhance):
    path = path_to_enhance.copy()
    best_distance = hamiltonian_path(Matrix, path)
    end = 0
    while end == 0:
        end = 1
        for i in range(0, len(Matrix)-1):
            for k in range(i + 1, len(Matrix)):
                if k - i == 1: continue
                new_path = path.copy()
                OPT2_swap2(new_path, i, k)
                new_distance = hamiltonian_path(Matrix, new_path)
                if new_distance < best_distance:
                    path = new_path.copy()
                    best_distance = new_distance
                    end = 0
                    break
            if end == 0: break
    return path

# def OPT2_alogrythm_input(Matrix, path):
#     new_path = path.copy()
#     best_distance = hamiltonian_path(Matrix, path)
#     end = 0
#     while end == 0:
#         end = 1
#         for i in range(0, len(Matrix) - 1):
#             for k in range(i + 1, len(Matrix)):
#                 if k - i == 1: continue
#                 OPT2_swap2(new_path.copy(), i, k)
#                 new_distance = hamiltonian_path(Matrix, new_path)
#                 if new_distance < best_distance:
#                     path = new_path.copy()
#                     best_distance = new_distance
#                     end = 0
#                     break
#             if end == 0: break
#     return path
