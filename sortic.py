from ListChanger import ListChanger
from CommandColors import CommandColors


def print_sortic_commands(arr_1):

    arr_2 = []
    sorted_arr = arr_1.copy()
    sorted_arr.sort()

    painter = CommandColors()

    if sorted_arr == arr_1:
        return True
    list = ListChanger(arr_1, arr_2)

    for i in range(len(arr_1)):
        arr_1_max = max(list.arr_1)

        while list.arr_1[0] != arr_1_max:
            list.ra()
            print(painter.dye_command('ra'))
        list.pb()
        print(painter.dye_command('pb'))

    for i in range(len(arr_2)):
        list.pa()
        print(painter.dye_command('pa'))
def main():
    arr = []
    value = input()

    while value != '!':
        number = int(value)
        arr.append(number)
        value = input()

    print_sortic_commands(arr)
main()
