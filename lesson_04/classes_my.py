from lesson_01.type_strigs import temperature


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
        return self.day_ripe <= 0


apple = Fruit("Apple", 2)
apple.describe()
apple.wait_a_day()
print(apple.is_ripe())
apple.wait_a_day()
print(apple.is_ripe())


class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.pi * self.radius ** 2


c1 = Circle(2)
c2 = Circle(5)

print("Area c1 is ", c1.area())
print("Area c2 is ", c2.area())

print("Pi is ", Circle.pi)


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def __str__(self):
        return f"Owner: {self.owner}, Balance: {self.__balance}"

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit {amount}. Balance:  {self.__balance}")
        else:
            print("Deposit can't be negative")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Not enough money on your account")
        else:
            self.__balance -= amount
            print(f"Withdraw {amount}. Balance:  {self.__balance}")

    def get_balance(self):
        return self.__balance


account = BankAccount("John", 100)
print(account)
account.deposit(100)
print(account)
account.withdraw(250)
account.withdraw(200)
# print(account.__balance)
print(account.get_balance())


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def make_sound(self, sound):
        print(f"{self.name} makes a sound: {sound}")

class Dog(Animal):
    #def make_sound(self):
      #  print(f"{self.name} says: Woof! ")

    def swim(self):
        print(f"{self.name} swims around.")

class Cat(Dog):
    def make_sound(self):
        print(f"{self.name} says: Meow! ")

    def play(self):
        print(f"I {self.name} can play with ball ")

dog = Dog("Doggi")
cat = Cat("Sima")
dog.eat()
dog.make_sound("Woof!")
cat.make_sound()
cat.play()
cat.eat()
dog.swim()
cat.swim()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Marks: {self.marks}"

student = Student("John", 25, 100)
print(student)

# perimetr (a+b)*2 area a*b

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle width: {self.width}, height: {self.height}"

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

r = Rectangle(10, 20)
print(r)
print(r.perimeter())
print(r.area())


#celsius
class Thermometer:
    def __init__(self):
        self.__temperature = -273

    def set_temperature(self, t):
        if t > -273:
            self.__temperature = t
        else:
            print("Thermometer can't lower -273")

    def get_temperature(self):
        return self.__temperature

term  = Thermometer()
print(term.get_temperature())
term.set_temperature(15)
print(term.get_temperature())