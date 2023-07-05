from entity import Animal


class AnimalService:
    def __init__(self):
        # We could, in theory, read the list of animals from a file
        self.__animal_list = [Animal("Rex", 4), Animal("Miti", 6), Animal("Dorel", 8)]

    def add_animal(self, new_animal):
        """
        Adds an animal to the animal list if it does not exist
        : param new_animal: Animal to be added (Animal)
        :return:
        """
        for animal in self.__animal_list:
            if animal == new_animal:
                raise ValueError(f'The Animal {animal} already exists!')
        self.__animal_list.append(new_animal)

    def __get_animal_position(self, animal):
        """
        Returns the position of a animal in the animal list, None if it doesn't exist
        :param animal_to_find: Animal to search for in the list (Animal)
        :return: The position of the animal if it is in the list (int), otherwise None
        """
        for i in range(len(self.__animal_list)):
            if self.__animal_list[i] == animal:
                return i
        return None

    def delete_animal(self, animal_to_delete):
        """
        Deletes an animal from the animal list
        :param animal_to_delete: Animal to delete from in the list (Animal)
        :return:
        """
        animal_index = self.__get_animal_position(animal_to_delete)
        if animal_index is None:
            raise ValueError(f'Animal {animal_to_delete} does not exist!')
        del self.__animal_list[animal_index]

    def get_all_animals(self):
        """
        Returns the list containing all the animals
        :return: The list of all the animals (list)
        """
        if len(self.__animal_list) == 0:
            raise ValueError("No animals!")
        return self.__animal_list

    def get_average_animal_age(self):
        """
        Returns the average of all the animals in the list
        :return: The average age of all the animals (float)
        """
        if len(self.__animal_list) == 0:
            raise ValueError("No animals!")

        age_sum = 0
        for animal in self.__animal_list:
            age_sum += animal.get_age()

        return age_sum / len(self.__animal_list)