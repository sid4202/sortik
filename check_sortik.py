from ListChanger import ListChanger
class SortikChecker:
    def __init__(self, arr_1):
        self.arr_1 = arr_1
        self.arr_2 = []

    def handle_operations(self, operation_str):
        commands = operation_str.split()

        list_changer = ListChanger(self.arr_1)

        for command in commands:
            command = "list_changer." + command + '()'

            eval(command)

        self.arr_1 =

    def check(self, operation_str):
        correct_sorted_arr_1 = self.arr_1.copy().sort()
        self.handle_operations(operation_str)

        if correct_sorted_arr_1 == self.arr_1






def main():