# 1. Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color. You must perform the following operations:

class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"{self.name} is {self.age} years old.")

    def get_info(self):
        print(f"{self.name}'s coat color is {self.coat_color}.")


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color, hunting_skill):
        super().__init__(name, age, coat_color)
        self.hunting_skill = hunting_skill

    def special_skill(self):
        print(f"{self.name} has a special skill: {self.hunting_skill}")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color, strength):
        super().__init__(name, age, coat_color)
        self.strength = strength

    def display_strength(self):
        print(f"{self.name}'s strength is {self.strength}.")


dog1 = Dog("puppy", 5, "black")
dog1.description()
dog1.get_info()
dog2 = JackRussellTerrier("tommy", 3, "Brown", "energetic")
dog2.description()
dog2.get_info()
dog2.special_skill()
dog3 = Bulldog("lucy", 4, "white", "quick & clever mind")
dog3.description()
dog3.get_info()
dog3.display_strength()
