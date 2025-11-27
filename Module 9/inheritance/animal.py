# class Superclass:
#
#      class Subclass(Superclass):

class Animal:
    def sound(self):
        print("Some generic animal sound.")


class Dog(Animal):
    def sound(self):
        print("woof woof")

class Cat(Animal):
    def sound(self):
        print("meow")


animal = Animal()
animal.sound()

Dog = Dog()
Dog.sound()

Cat = Cat()
Cat.sound()
