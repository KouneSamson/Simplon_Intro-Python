#%% Pet Names

animaux = {"Polgara" : "Dog",
           "Calisson": "Rat",
           "Aldwin"  : "Cat"}

for nom, espece in animaux.items() :
    print("%s is a %s." % (nom,espece))

#%% Polling Friends

rpgRoles = {"Mélissa" : "Damage Dealer",
            "Morgan" : "Tank",
            "Romain" : "Healer"}

print("What is your favorite Role in an RPG ?")

for nom, role in rpgRoles.items() :
    print("%s likes to be a %s." % (nom,role))

#%% Pet Names 2

animaux = {"Polgara" : "Dog",
           "Calisson": "Rat",
           "Aldwin"  : "Cat"}

def printDico(dico):
    for key, value in dico.items() :
        print("%s --> %s" % (key,value))


printDico(animaux)

animaux["Polgara"] = "Autralian Shepherd"

print("")
printDico(animaux)

animaux["Carillon"] = "Crow"

print("")
printDico(animaux)

del animaux["Carillon"]

print("")
printDico(animaux)

#%% Weight Lifting

fitness = {"Bench Press" : 5,
           "Squat" : 10,
           "Hip Thrust" : 20}

printDico(fitness)

fitness["Hip Thrust"] = 35

print("")
printDico(fitness)

fitness["Dead Lift"] = 1

print("")
printDico(fitness)

del fitness["Bench Press"]

print("")
printDico(fitness)

#%% Mountain Height 1 et 2

tallMountain = {"Mount Evrest" : 8848,
                "K2"           : 8611,
                "Kangchenjunga": 8586,
                "Lhotse"       : 8516,
                "Makalu"       : 8485}

print("List of Moutain Names : ")
for k in tallMountain.keys() :
    print(k)

print("")
print("List of Mountain Heights :")
for v in tallMountain.values():
    print(v)

print("")
print("5 tallest Mountains in the World :")
for k in sorted(tallMountain.keys()):
    v = tallMountain[k]
    print("%s is %d meters tall." % (k,v))

#%% Mountain Height 3

def metersToFeet(m):
    return (m*3.28)

tallMountain = {"Mount Evrest" : [8848,int(metersToFeet(8848))],
                "K2"           : [8611,int(metersToFeet(8611))],
                "Kangchenjunga": [8586,int(metersToFeet(8586))],
                "Lhotse"       : [8516,int(metersToFeet(8516))],
                "Makalu"       : [8485,int(metersToFeet(8485))]}

print("List of Moutain Names : ")
for k in tallMountain.keys() :
    print("\t- %s" % k)

print("")
print("List of Heights in meters :")
for k in tallMountain.keys() :
    print("\t- %s" % tallMountain[k][0])

print("")
print("List of Heights in meters :")
for k in tallMountain.keys() :
    print("\t- %s" % tallMountain[k][1])


















