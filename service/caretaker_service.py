from domain.caretaker import Caretaker
from repository.repository import Repository


class CaretakerService:
    def __init__(self, repository: Repository):
        self.__repository = repository

    def add_caretaker(self, name, age, animal_name):
        caretaker = Caretaker(name, age, animal_name)
        self.__repository.add(caretaker)

    def delete_caretaker(self, name):
        caretaker = Caretaker(name, 0, "")
        self.__repository.delete(caretaker)

    def get_all_caretakers(self):
        return self.__repository.get_all()

