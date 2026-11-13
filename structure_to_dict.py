# Converting a structure (list of tuples) into a dictionary

students = [("Amit", 85), ("Riya", 92), ("Karan", 78)]

student_dict = dict(students)

print("Original structure:", students)
print("Dictionary:", student_dict)

# Converting a list of objects into dictionaries
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s = Student("Neha", 88)
s_dict = {"name": s.name, "marks": s.marks}
print("Object as dictionary:", s_dict) 