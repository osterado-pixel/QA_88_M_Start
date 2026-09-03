class Fruit:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


fruit1 = Fruit("Apple", 10)
fruit2 = Fruit("Banana", 20)

print(fruit1.name, fruit1.weight)
print(fruit2.name, fruit2.weight)
fruit1.weight = 40
print(fruit1.name, fruit1.weight)


class Fruit:
    def __init__(self, name, day_ripe):
        self.name = name
        self.day_ripe = day_ripe

    def describe(self):
        print(f"This is a {self.name}")

    def wait_a_day(self):
        self.day_ripe -= 1
        print(f"{self.name} day ripe: {self.day_ripe}")

    def is_ripe(self):
        return self.day_ripe <=0
