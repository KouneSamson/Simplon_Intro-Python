class Person :
    def __init__(self, name = "", age = 0, placeOfBirth = "", favFood = "") :
        self.name = name
        self.age = age
        self.placeOfBirth = placeOfBirth
        self.favFood = favFood
        
    def presentation(self) :
        print("Hello, my name is %s, i am %d years old, i was born in %s and i like to eat %s" % (self.name, self.age, self.placeOfBirth, self.favFood))


class Student(Person):
    def __init__(self,
                 name = "", age = 0, placeOfBirth = "", favFood = "",
                 domaineEtude = "", ecole = ""):
        super().__init__(name,age,placeOfBirth,favFood)
        self.domaineEtude = domaineEtude
        self.ecole = ecole
