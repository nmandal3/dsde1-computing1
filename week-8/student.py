
class DesEngStudent:
    def __init__(self, name, year, budget):
        self.n = name
        self.yr = year
        self.b = budget
    
    def print(self):
        statement = "{} (DE{}) with £{} remaining"
        return statement.format(str(self.n), str(self.yr), str(self.b))
    
    def spend(self, amount):
        if amount <= self.b:
            remainder = self.b - amount
            return remainder
        else:
            raise ValueError
    
    def three_d(self, a):
        return self.spend(5.50*a)

    def paper_print(self, a):
        return self.spend(0.10*a)

    def laser_cut(self, a):
        return self.spend(a)

