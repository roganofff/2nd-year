from salary import hourly_salary

quit_ = 'q'
quit_msg = f' [{quit_} to quit]'

while True:
    position = input(f'Position in company{quit_msg} : ')
    if position == quit_: break
    hours = input(f'Actual hours{quit_msg}: ')
    if position == quit_: break


    try:
        hours = float(hours)
    except ValueError:
        print('Value is not a number or decimal point is not a dot.')
        continue

    try:
        salary, tax = hourly_salary(position, hours)
    except Exception as error:
        print(error)
    else:
        print(f'Salary after tax: {salary}')
        print(f'Tax: {tax}')