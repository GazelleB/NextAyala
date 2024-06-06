from Animals import *
# from Animals import Cat
# from Animals import Dog
# from Animals import Dragon
# from Animals import Skunk
# from Animals import Unicorn

dog = Dog("Brownie", 10)
cat = Cat("Zelda", 3)
skunk = Skunk("Stinky", 0)
unicorn = Unicorn("Keith", 7)
dragon = Dragon("Lizzy", 1450)
dog2 = Dog("Doggo", 80)
cat2 = Cat("Kitty", 80)
skunk2 = Skunk("Stinky Jr.", 80)
unicorn2 = Unicorn("Clair", 80)
dragon2 = Dragon("McFly", 80)

zoo_lst = [dog, cat, skunk, unicorn, dragon,
           dog2, cat2, skunk2, unicorn2, dragon2]
for animal in zoo_lst:
    # if teh animal hungry' feeds her and print her name
    if animal.is_hungry():
        print(animal.__class__.__name__, animal.get_name())
        while animal.is_hungry():
            animal.feed()
        animal.talk()

        # calling the special function in each class
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()

print(Animal.zoo_name)
