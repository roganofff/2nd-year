directions = {
    'N': 'S',
    'S': 'N',
    'E': 'W',
    'W': 'E'
}

def path(path: str):
    path = list(path)
    while True:
        i = 0
        to_del = -1

        while i < len(path) - 1:
            if directions[path[i]] == path[i + 1]:
                to_del = i
                break
            i += 1
        if to_del >= 0:
            path.pop(to_del)
            path.pop(to_del)
        else:
            break

    return ''.join(path)