class person:
    
    def __init__(self, id, name, age, gender):
        ## instantiating the 'Inner' class
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        

    def show(self):
        print(self.id, self.name, self.age, self.gender)
        
    
    class student:
        def __init__(self, roll, lesson, score):
        ## instantiating the 'Inner' class
            self.roll = roll
            self.lesson = lesson
            self.score = score
        
        def show(self):
            print(self.roll, self.lesson, self.score)

person1 = person(1, 'Jane', 19, 'female')
person2 = person(2, 'Gerwin', 20, 'male')

st1 = person1.student('2. stage', 'Math', 'B')
st2 = person2.student('1. stage', 'Chemistry', 'A')
person1.show()
st1.show()

