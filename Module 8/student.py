class student:
    school_name = "Digital School"
    def __init___(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

student_1 = Student("Alice", 15 , "Python")
student_2 = Student("Bob", 16 , "Javascript")

print(student_1.course)
print(student_2.course)
