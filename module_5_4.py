class House:
    house_history = []

    def __new__(cls, *args, **kwargs):
        cls.house_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.number_of_floors = self.number_of_floors + value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        self.number_of_floors += value
        return self

    def go_to(self, new_floor: int):
        if 1 < new_floor <= self.number_of_floors:
            print(f"{new_floor}")
        else:
            print("Такого этажа не существует")

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")


h1 = House('ЖК Горский', number_of_floors=10)
h2 = House('Домик в деревне', number_of_floors=20)

del h1
del h2

print(House.house_history)
