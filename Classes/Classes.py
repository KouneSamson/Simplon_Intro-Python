#%% Rocket With No Class

x = y = 0
rocket1 = [x,y]
rocket2 = [x,y]
rocket3 = [x,y]
rocket4 = [x,y]
rocket5 = [x,y]

ensembleRocket = [rocket1,rocket2,rocket3,rocket4,rocket5]

#%% Your Own Rocket

class Rocket :
    def __init__(self) :
        self.x = 0
        self.y = 0
    def move_up(self) :
        self.y += 1

r = Rocket()

print(r)
print(r.y)
r.move_up()
print(r.y)

flotte = [ Rocket() for rock in range(1,6) ]    

for ro in flotte : print(ro)

#%% Your Own Rocket 2

class Rocket2 :
    def __init__(self,x = 0, y = 0) :
        self.x = x
        self.y = y
    
    def move(self, x , y):
        self.x += x
        self.y += y
        
    def getDistance(self , ro) :
        dist = ((ro.x - self.x)**2 + (ro.y - self.y)**2)**(1/2)
        return dist


def printPos(rocket) :
    print("x : %d | y : %d\n" % (rocket.x,rocket.y))

r1 = Rocket2()
printPos(r1)
r1.move(2,0)
printPos(r1)
r1.move(1,5)
printPos(r1)

flotte = [ Rocket2() for rock in range(1,6) ]

for i in range(0,5) :
    flotte[i].move(i,-i)
    print("Rocket #%d" % i)
    printPos(flotte[i])

distance = r1.getDistance(flotte[0])
print("distance entre r1 et f0 : %d " % distance)

distance = r1.getDistance(flotte[1])
print("distance entre r1 et f1 : %d " % distance)

distance = flotte[0].getDistance(flotte[3])
print("distance entre f0 et f3 : %d " % distance)

#%% Rocket Attributes

class Rocket3 :
    def __init__(self,x = 0, y = 0, colour = 0x000000) :
        self.x = x
        self.y = y
        self.colour = hex(colour)
    
    def move(self, x , y):
        self.x += x
        self.y += y
        
    def getDistance(self , ro) :
        dist = ((ro.x - self.x)**2 + (ro.y - self.y)**2)**(1/2)
        return dist

r3 = Rocket3(colour = 0xFFFFFF)
print(r3.colour)

red = Rocket3(colour = 0x00FFFF)
green = Rocket3(colour = 0xFF00FF)
blue = Rocket3(colour = 0xFFFF00)

print(red.colour)
print(green.colour)
print(blue.colour)

#%% Rocket Methods

class Rocket4 :
    def __init__(self,x = 0, y = 0, colour = 0x000000) :
        self.x = x
        self.y = y
        self.colour = hex(colour)
    
    def move(self, x , y):
        self.x += x
        self.y += y
        
    def getDistance(self , ro) :
        dist = ((ro.x - self.x)**2 + (ro.y - self.y)**2)**(1/2)
        return dist
    
    def shoot(self):
        print("PEW !! PEW !!")

r4 = Rocket4()
r4.shoot()

#%% Person Class

class Person :
    def __init__(self, name = "", age = 0, placeOfBirth = "", favFood = "") :
        self.name = name
        self.age = age
        self.placeOfBirth = placeOfBirth
        self.favFood = favFood
        
    def presentation(self) :
        print("Hello, my name is %s, i am %d years old, i was born in %s and i like to eat %s" % (self.name, self.age, self.placeOfBirth, self.favFood))

p1 = Person("Victor",27,"Metz","Donburi")

print(p1)
p1.presentation()

#%% Car Class

class Car :
    def __init__(self,marque="",model="",nbMotrice=2,nbPorte=3,radar=False) :
        self.marque = marque
        self.model = model
        self.nbMotrice = nbMotrice
        self.nbPorte = nbPorte
        self.radar = radar
    
    def description(self) :
        print("%s  |  %s" % (self.marque, self.model))
        print("\t Roues Motrices : %d" % self.nbMotrice)
        print("\t Portes : %d" % self.nbPorte)
        if self.radar :
            print("\t Radar de Recul : oui")
        else :
            print("\t Radar de Recul : non")

c1 = Car("Jaguar","XE", 2, 5, True)
c2 = Car("Renault","Twingo", 2, 3, False)

c1.description()
c2.description()

#%% Student Class

class Student(Person):
    def __init__(self,
                 name = "", age = 0, placeOfBirth = "", favFood = "",
                 domaineEtude = "", ecole = ""):
        super().__init__(name,age,placeOfBirth,favFood)
        self.domaineEtude = domaineEtude
        self.ecole = ecole
    
stud = Student("Victor",27,"Metz","Ramen","Informatique","Simplon.co")
stud.presentation()
print(stud.domaineEtude + " in " + stud.ecole)

#%% Refining Shuttle
"""
class Rocket4 :
    def __init__(self,x = 0, y = 0, colour = 0x000000) :
        self.x = x
        self.y = y
        self.colour = hex(colour)
    
    def move(self, x , y):
        self.x += x
        self.y += y
        
    def getDistance(self , ro) :
        dist = ((ro.x - self.x)**2 + (ro.y - self.y)**2)**(1/2)
        return dist
    
    def shoot(self):
        print("PEW !! PEW !!")
"""
class Shuttle(Rocket4):
    def __init__(self,
                 x = 0, y = 0, colour = 0x000000,
                 volTermine = 0, ISSdock = False, nbVolMax = 2):
        super().__init__(x,y,colour)
        self.volTermine = volTermine
        self.ISSdock = ISSdock 
        self.nbVolMax = nbVolMax
    
    def docking(self):
        if not self.ISSdock:
            print("You can't dock to the ISS")
        else:
            print("Docking in process ...")
    
shut = Shuttle(0,0,0,5,True,10)
shut.docking()

    
    

































