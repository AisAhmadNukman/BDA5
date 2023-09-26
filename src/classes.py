class park:
    def __init__(self, area, hari, jam, jk, kpdtn, p_jk, p_kpdtn):
        self.area = area
        self.hari = hari
        self.jam = jam
        self.jk = jk
        self.kpdtn = kpdtn
        self.p_jk = p_jk
        self.p_kpdtn = p_kpdtn

    def display_variables(self):
        print(f"Variable 1: {self.area}")
        print(f"Variable 2: {self.hari}")
        print(f"Variable 3: {self.jam}")