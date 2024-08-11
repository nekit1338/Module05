class House:
    house_history = []

    def __new__(cls, *args, **kwargs):
        cls.house_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")


h1 = House('ЖК Горский', number_of_floors=10)
h2 = House('Домик в деревне', number_of_floors=20)

del h1
del h2

print(House.house_history)
