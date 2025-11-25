class MyClass:
    def __init__(self):
        self.__public.variable = "This is a private variable"



my_class = MyClass()

print(my_class.__private_variable)
print(my_class.__private_variable())