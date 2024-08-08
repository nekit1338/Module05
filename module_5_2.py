class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def go_to(self, new_floor: int):
        if 1 < new_floor <= self.number_of_floors:
            print(f"{new_floor}")
        else:
            print("Такого этажа не существует")


schweine = House('ЖК Горский', 18)
goat = House('Домик в деревне', 2)

#  __str__
print(schweine)
print(goat)

#  __len__
print(len(schweine))
print(len(goat))
