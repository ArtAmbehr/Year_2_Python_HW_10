# Задание 1. 
# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики. 


class Animal:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print("Данное животное неизвестно.")


class Dog (Animal):
    def __init__(self, name, habitat):
        super().__init__(name)
        self.habitat = habitat

    def display_info(self):
        print(f"Это собака по кличке {self.name}. Она живет в {self.habitat}.")


class Cat(Animal):
    def __init__(self, name, length):
        super().__init__(name)
        self.length = length

    def display_info(self):
        print(f"Это кошка по имени {self.name}. Ее длина {self.length}.")


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, name, **kwargs):
        if animal_type == "Dog":
            return Dog(name, kwargs.get("habitat"))
        elif animal_type == "Cat":
            return Cat(name, kwargs.get("length"))
        else:
            return Animal(name)


# Использование:
dog = AnimalFactory.create_animal("Dog", "Шарик", habitat="доме")
dog.display_info()

cat = AnimalFactory.create_animal("Cat", "Барсик", length="50 см")
cat.display_info()

animal = AnimalFactory.create_animal("Animal", "Неизвестное животное")
animal.display_info()
