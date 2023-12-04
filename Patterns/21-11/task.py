def f1(line):
    result = []
    result.append(line[0])
    for i in range(1, len(line) - 1):
        if line[i - 1] != line[i]:
            result.append(line[i])
    return result

line = '1223144'
print(f1(line))