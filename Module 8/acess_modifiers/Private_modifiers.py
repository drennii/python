class MyClass:
    def __init__(self):
        self.__private.variable = "This is a private variable"

    def __private_method(self):
        print("This is a private variable")

my_class = MyClass()

print(my_class.__private_variable)
print(my_class.__private_variable())