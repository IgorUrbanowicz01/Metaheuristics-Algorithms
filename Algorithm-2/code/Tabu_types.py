def invert(path, i, j):
    new_path = path.copy()
    while i < j:
        new_path[i], new_path[j] = new_path[j], new_path[i]
        i += 1;
        j -= 1;
        return new_path

def swap(path, i, j):
    new_path = path.copy()
    new_path[i], new_path[j] = new_path[j], new_path[i]
    return new_path


def insert(path, i, j):
    new_path = path.copy()
    tmp = new_path[i]
    del new_path[i]
    new_path.insert(j, tmp)
    return new_path


def reverse_insert(path, i, j):
    new_path = path.copy()
    tmp = new_path[j]
    del new_path[j]
    new_path.insert(i, tmp)
    return new_path