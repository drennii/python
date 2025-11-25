class MyClass:
    def __init__(self):
        self.protected.variable = "This is a private variable"



my_class = MyClass()

print(my_class.protected)
print(my_class.protected())