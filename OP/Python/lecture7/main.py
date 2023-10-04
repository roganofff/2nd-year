from typing import List

def detective(password: str) -> List[str]:
    answer = list()
    
    varies = {
        '1': ('2', '4'),
        '2': ('1', '3', '5'),
        '3': ('2', '6'),
        '4': ('1', '5', '7'),
        '5': ('2', '4', '6', '8'),
        '6': ('5', '3', '9'),
        '7': ('4', '8'),
        '8': ('5', '7', '9'),
        '9': ('8', '6'),
        '0': ('8', )
    }

    for i in range(len(password)):
        for value in varies.get(password[i]):
            temp = password
            for digit in value:
                answer.append(temp[:i] + digit + temp[i+1:])
    answer.insert(0, password)

    return answer


print(detective('123'))