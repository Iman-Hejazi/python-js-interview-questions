'''
given the Bird, Dog, and Cat classes:
1) using ABC, write an interface class "Animal" that should be used as a parent of all of these classes
2) use 'abstractmethod' to define the "make_sound" function inside the interface class
3) write a docstring for the abstractmethod function inside the interface
4) write a "Factory method class" to instantiate the three animal classes
5) write a function in the factory class that gets a string as an input and returns the related animal instance
'''


from abc import ABC, abstractmethod

# modify the Animal class as required


class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        """Implement the sound of the animal
        """
        pass


class Bird(Animal):
    def __init__(self) -> None:
        pass

    def make_sound(self) -> None:
        print('make bird sound')

    def fly(self, distance: int) -> None:
        print(f'Bird flies {distance} meters')


class Dog(Animal):
    def __init__(self) -> None:
        pass

    def make_sound(self) -> None:
        print('make dog sound')

    def run(self, distance: int) -> None:
        print(f'Dog runs {distance} meters')


class Cat(Animal):
    def __init__(self) -> None:
        pass

    def make_sound(self) -> None:
        print('make cat sound')

    def walk(self, distance: int) -> None:
        print(f'Cat walks {distance} meters')

# modify this Factory class as required


class Factory:

    def __init__(self) -> None:
        self._dog_exit = None

    def facotry_method(self, animal_type: str = 'dog') -> Animal:
        """
        This method takes a string as input and returns an instance of
        the corresponding Animal class.

        Args:
            animal_type (str): The type of animal ("bird", "dog", or "cat").

        Returns:
            Animal: An instance of the corresponding animal class.
        """
        if animal_type == 'dog':
            if self._dog_exit:
                return self._dog_exit

            self._dog_exit = Dog()
            return self._dog_exit

        if animal_type == 'cat':
            return Cat()
        if animal_type == 'bird':
            return Bird()


factory = Factory()
my_dog = factory.facotry_method('dog')
my_dog.make_sound()

my_dog_2 = factory.facotry_method('dog')
print(f'Is dog 1 is equal to dog 2:  {my_dog is my_dog_2}')
