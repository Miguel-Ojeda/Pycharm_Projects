class Animal:
    def __init__(self, name):
        self.name = name
        self.animal = "animal"

    def display_name(self):
        print("Soy un", self.animal, "y me llamo", self.name)

    def speak(self):
        self.display_name()
        print("No sé hablar")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.animal = "perro"

    def speak(self):
        super().display_name()
        print("Hago guau, guau")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.animal = "gato"

    def speak(self):
        super().display_name()
        print("Hago miau, miau")

pet_list = []
animal_1 = Animal("Juanito")
pet_list.append(animal_1)
animal_2 = Animal("Pepito")
pet_list.append(animal_2)
gato_1 = Cat("Jimmy")
pet_list.append(gato_1)
perro_1 = Dog("Eustaquio")
pet_list.append(perro_1)

for animal in pet_list:
    animal.speak()
