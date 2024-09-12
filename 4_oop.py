'''
1) make a parent class named "Employee" that get a name as input in constructor
2) make a child class named "JuniorDev" extends Employee which has a "level" variable equal to 1
3) instantiate a JuniorDev object with name "John"
4) change John's level to 2
'''


class Employee:
    """This Employee class
    """

    def __init__(self, name: str) -> None:
        self.name = name


class JuniorDev(Employee):
    """A child class representing a Junior Developer.
    Version 1
    """
    _level = 1

    def __init__(self, name: str) -> None:
        super().__init__(name)

    @classmethod
    def update_level(cls, new_value: int):
        """
        Updates the level for all instances of JuniorDev (class-level update).

        Args:
            new_value (int): The new level value to set.
        """
        cls._level = new_value

    @classmethod
    def get_level(cls):
        """
         Retrieves the current class-level of JuniorDev.

         Returns:
             int: The current level shared by all instances.
         """
        return cls._level


# In Version 2, the level is defined as an instance variable.
# This means that every time I create a new object from the JuniorDevVersion2 class,
# a separate level is assigned to that specific object. This contrasts with Version 1,
#  where level is shared across all instances.

class JuniorDevVersion2(Employee):
    """A child class representing a Junior Developer.
        Version 2
    """

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._level = 1

    def update_level(self, new_value: int):
        """
        Updates the level of the JuniorDev object.

        Args:
            new_value (int): The new level value to set for the junior developer.
        """
        self._level = new_value

    def get_level(self):
        """
        Retrieves the current level of the JuniorDev object.

        Returns:
            int: The current level of the junior developer.
        """
        return self._level


#########################################
# Using Version 1: class variable
junior_dev = JuniorDev('John')
print(junior_dev.get_level())
junior_dev.update_level(2)
print(junior_dev.get_level())

#########################################
# Using Version 2: instance variable
junior_dev1 = JuniorDevVersion2('Alice')
junior_dev2 = JuniorDevVersion2('Bob')
junior_dev1.update_level(2)
print(junior_dev1.get_level())
print(junior_dev2.get_level())
