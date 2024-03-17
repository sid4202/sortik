from termcolor import colored


class CommandColors:
    def __init__(self):
        self.s_commands = ['sa', 'sb', 'ss']
        self.p_commands = ['pa', 'pb']
        self.r_commands = ['ra', 'rb', 'rr']
        self.rr_commands = ['rra', 'rrb', 'rrr']

    def dye_command(self, command):
        if command in self.s_commands:
            return colored(command, 'green')

        if command in self.p_commands:
            return colored(command, 'blue')

        if command in self.r_commands:
            return colored(command, 'cyan')

        if command in self.rr_commands:
            return colored(command, 'light_cyan')
