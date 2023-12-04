def pyramide_path(pyramide):
    max_level = len(pyramide) - 1
    all_paths = []
    cur_path = []
    def dfs(level, ind, cur_path):
        cur_path.append(str(pyramide[level][ind]))
        if level < max_level:
            dfs(level + 1, ind, cur_path.copy())
            dfs(level + 1, ind + 1, cur_path.copy())
        else:
            all_paths.append(''.join(cur_path.copy()))
            cur_path.pop()
    dfs(0, 0, cur_path)
    return all_paths

pyramide1 = [[1], [2, 3], [4, 5, 6]]
pyramide2 = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 0]]
print(pyramide_path(pyramide2))