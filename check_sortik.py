from ListChanger import ListChanger
from CommandColors import CommandColors


class SortikChecker:
    def __init__(self, arr_1):
        self.arr_1 = arr_1
        self.arr_2 = []

    def handle_operations(self, commands):
        list_changer = ListChanger(self.arr_1, self.arr_2)

        for command in commands:
            command = "list_changer." + command + '()'

            eval(command)
        print(self.arr_1)

        self.arr_1 = list_changer.arr_1
        self.arr_2 = list_changer.arr_2

    def check(self, operation_str):
        correct_sorted_arr_1 = self.arr_1.copy()
        correct_sorted_arr_1.sort()

        self.handle_operations(operation_str)

        print(correct_sorted_arr_1)
        if correct_sorted_arr_1 == self.arr_1:
            print("CORRECT")
        else:
            print("NOT CORRECT")


def main():
    arr = []

    value = input()

    painter = CommandColors()

    while value != '!':
        number = int(value)

        arr.append(number)

        value = input()

    commands = []

    command = input()

    while command != "*":
        commands.append(command)

        command = input()
        print(painter.dye_command(command))

    checker = SortikChecker(arr)

    checker.check(commands)


main()
