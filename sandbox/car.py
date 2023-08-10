class Car:
    def __init__(self, mark, model):
        self.mark = mark
        self.model = model
        self.li = []

    def add(self, li_of_tuple):
        self.li = [Car(*t) for t in li_of_tuple]

    def __repr__(self) -> str:
        return str(self.__dict__)


li = [("Audi", "A4"), ("BMW", "M3"), ("Mercedes", "C63")]
car = Car("Renault", "Clio")
