from typing import Dict, Tuple, List, Callable

things = {
    'iPhone 14': 15,
    'Poco Phone mega 3': 1000,
    'Xiaomi Redmi Note 4x': 167,
    'iPhone 12 mini': 555,
    'iPhone 7': 2,
    'iPhone 15 pro max 1tb titan black': 999,
    'Samsung Galaxy 7 edge': 1
}



def top_iphone(products: Dict) -> List:
    def is_iphone(phones: Tuple) -> bool:
         return str(phones[0]).lower().startswith('iphone')

    iphones = list(filter(is_iphone, products.items()))
    iphones = sorted(iphones, key=lambda x: x[1], reverse=True)

    return [name for name, _ in iphones[:3]]


# print(top_iphone(things))




staff = {
     'hr_abc': 10,
     'hr_qwerty': 20,
     'it_hello': 39
}

def round_(func: Callable) -> Callable:
    def new(*args, **kwargs):
         return round(func(*args, **kwargs), 2)
    return new


@round_
def avg_salary_of_department(staff: Dict, department: str) -> float:
     avg = 0

     def dep_filter(values: Tuple) -> int|float:
          return str(values[0]).lower().startswith(department)

     dep_staff = list(filter(dep_filter, staff.items()))
     return sum([salary for _, salary in dep_staff]) / len(dep_staff)


# print(avg_salary_of_department(staff, 'it'))


staff = {
     'Karateev': 1000,
     'Yeltsin': 10000,
     'Tsverkunov': 98,
     'Kuznetsova': 99,
     'Turin': 4123724,
     'Lee': 228133766,
     'Ng': 9999999999
}

def format_salary(staff: dict) -> List[str]:
     salary_list = []

     for employee, salary in staff.items():
          salary_list.append(f'{employee}: {salary} руб.')

     return salary_list

# print(format_salary(staff))


def format_salary_(employee: tuple) -> str:
     return f'{employee[0]}: {employee[1]} руб.'


print(list(map(format_salary_, staff.items())))