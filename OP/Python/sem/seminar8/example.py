from typing import Any

def task(*args: tuple[dict[str, int|float]]) -> dict[str, int|float]:
    result = dict()
    for arg in args:
        for key, value in arg.items():
            if key in result.keys():
                result[key] += value
            else:
                result[key] = value

    return result


def task2(first: list[Any], second: list[Any]) -> list:
    # 1
    # result = []
    # for value in first:
    #     if value not in second:
    #         result.append(value)
    # for value in second:
    #     if value not in first:
    #         result.append(value)
    
    # 2

    intersection = set(first) & set(second)
    return [value for value in first + second if value not in intersection]
