# Пространство имён - это раздел, внутри которого имя уникально 
# и не связано с такими же именами в других пространствах имён

# Каждая функция определяет собственное пространство имён.

short_list = [1, 2, 3]

while True:
    value = input('Position [q to quit]: ')

    if value == 'q':
        break
    try:
        pos = int(value)
        print(short_list[pos])
    except IndexError:
        print("Bad index:", pos)
    except Exception as other:
        print("Something went wrong:", other)