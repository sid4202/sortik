class ListChanger:
    def __init__(self, arr_1, arr_2):
        self.arr_1 = arr_1
        self.arr_2 = arr_2

    def sa(self):
        if self.arr_1.length < 2:
            return

        self.arr_1[0], self.arr_1[1] = self.arr_1[1], self.arr_1[0]

    def sb(self):
        if self.arr_2.length < 2:
            return

        self.arr_2[0], self.arr_2[1] = self.arr_2[1], self.arr_2[0]

    def ss(self):
        self.sa()
        self.sb()

    def pa(self):
        if not self.arr_2:
            return

        self.arr_1.insert(0, self.arr_2[0])

    def pb(self):
        if not self.arr_1:
            return

        self.arr_2.insert(0, self.arr_1[0])

    def ra(self):
        if not self.arr_1:
            return

        self.arr_1 = self.arr_1[1:] + self.arr_1[:1]
    def rb(self):
        if not self.arr_2:
            return

        self.arr_2 = self.arr_2[1:] + self.arr_2[:1]

    def rr(self):
        self.ra()
        self.rr()

    def rra(self):
        self.arr_1 = self.arr_1[-1:] + self.arr_1[:-1]

    def rrb(self):
        self.arr_2 = self.arr_2[-1:] + self.arr_2[:-1]


    def rrr(self):
        self.rra()
        self.rrb()
