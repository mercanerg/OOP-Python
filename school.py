class Person:
    """Outer Class"""

    def __init__(self, id, name, age, gender):
        ## instantiating the 'Inner' class
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
    
    def student(self, student_id, stage):
        self.student_id = student_id
        self.stage = stage
            

    def teacher(self, employee_id, department, lesson):
            self.employee_id = employee_id
            self.department = department
            self.lesson = lesson
    
st1 = Person(1,'John', 17, 'male')
print(st1.name)