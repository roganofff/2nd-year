def find_path(matrix: list):
    n = len(matrix)
    cord_x = cord_t = None
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 'x':
                cord_x = i, j
            elif matrix[i][j] == 't':
                cord_t = i, j
    
    hor_shift = cord_t[1] - cord_x[1]
    hor_dir = 'W' if hor_shift < 0 else 'E'
    ver_shift = cord_t[0] - cord_x[0]
    ver_dir = 'N' if ver_shift < 0 else 'S'

    return hor_dir * abs(hor_shift) + ver_dir * abs(ver_shift)


matrix = [
    ['0', '0', 'x'],
    ['0', '0', '0'],
    ['t', '0', '0']
]

print(find_path(matrix))