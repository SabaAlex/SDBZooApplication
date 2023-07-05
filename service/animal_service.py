from domain.animal import Animal
from repository.repository import Repository


class AnimalService:
    def __init__(self, repository: Repository):
        self.__repository = repository

    def add_animal(self, name, age):
        animal = Animal(name, age)
        self.__repository.add(animal)

    def animal_exists(self, animal_name):
        return self.__repository.find_position(Animal(animal_name, 0)) is not None

    def delete_animal(self, name):
        animal = Animal(name, 0)
        self.__repository.delete(animal)

    def get_all_animals(self):
        return self.__repository.get_all()

    def get_average_animal_age(self):
        animal_list = self.__repository.get_all()
        age_sum = 0
        for animal in animal_list:
            age_sum += animal.get_age()
        return age_sum / len(animal_list)
