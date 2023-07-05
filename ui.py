from entity import Animal
from service import AnimalService

class AnimalUI:
    def __init__(self, service: AnimalService):
        self.__service = service

    def __print_menu(self):
        print("1.Add animal")
        print("2.Delete animal")
        print("3.Average zoo age")
        print("4.Show all animals")
        print("0.Exit")

    def __validate_age(self, age: str):
        try:
            int(age)
        except Exception:
            raise ValueError("Age is not a number!")

    def __add_animal(self):
        name = input("Animal name: ")
        age = input("Animal age: ")

        self.__validate_age(age)

        self.__service.add_animal(Animal(name, int(age)))

    def __delete_animal(self):
        name = input("Animal name to delete : ")
        age = input("Animal age to delete : ")

        self.__validate_age(age)

        self.__service.delete_animal(Animal(name, int(age)))

    def __average_animal_age(self):
        print(f'The average age of all the animals is {self.__service.get_average_animal_age()}')

    def __show_all_animals(self):
        for animal in self.__service.get_all_animals():
            print(animal)

    def run(self):
        while True:
            self.__print_menu()
            try:
                command = int(input("Choose the command: ").strip())
                if command == 0:
                    break
                elif command == 1:
                    self.__add_animal()
                elif command == 2:
                    self.__delete_animal()
                elif command == 3:
                    self.__average_animal_age()
                elif command == 4:
                    self.__show_all_animals()
            except Exception as error:
                print(error)
