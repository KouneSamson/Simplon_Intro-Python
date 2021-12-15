#%% Alphabet

alphabet = ["a","b","c","d","e","f","g","h","i","j"]

print(alphabet[:3])
print(alphabet[3:6])
print(alphabet[6:])

#%% Awesomness

fiveNames = ["Victor","Mélissa","Pascale","Luc","Polgara"]
awesomeNames = [name + " is awesome!" for name in fiveNames]
print(awesomeNames)

#%% Cubes

cubesDix = [num**3 for num in range(1,11)] ; print(cubesDix)

#%% Famous People

famous = ["Poe","Lovecraft","Asimov","Brin"]
famous.pop()
famous.pop(0)
del famous[1]
famous.remove("Lovecraft")
print("il reste " + str(len(famous)) + " célébrité dans la liste famous.")

#%% Finding Python

monty = "Le langage Python porte son nom en l'honneur de la troupe des Monty Python"
print("Python" in monty)
print(monty.find("Python"))
print(monty.rfind("Python"))
print(monty.count("Python"))
montyspliton = monty.split()
print(montyspliton)
for mot in montyspliton : print(mot)
print(monty.replace("Python","Ruby"))

#%% First List

langages = ['python','c','java']

# First List
print(langages[0])
print(langages[1])
print(langages[2])

#%% First List Loop

langages = ['python','c','java']

for i in range(len(langages)) :
    print(langages[i])

#%% First Neat List

langages = ['python','c','java']

print("Le langage " + langages[0] + " est plutôt pas mal.")
print("Le langage " + langages[1] + " est plutôt pas mal.")
print("Le langage " + langages[2] + " est plutôt pas mal.")

#%% First Neat List Loop

langages = ['python','c','java']

for i in range(len(langages)) :
    print("Le langage " + langages[i] + " est plutôt pas mal.")

#%% First Twenty

nombres = list(range(1,21))
print(nombres)

#%% Five Wallets

wallets = [255,1000,53,10,666]
print("The fattest wallet has " + str(max(wallets)) + " in it.")
print("The skinniest wallet has " + str(min(wallets)) + " in it.")
print("All together, these wallets have " + str(sum(wallets)) + " in them.")

#%% Gymnast Scores

scoresGym = (1,2,3,4,5,6,7,8,9,10)
print("The lowest possible score is %d, and the highest possible score is %d." % (min(scoresGym),max(scoresGym)))
for score in scoresGym :
    if score != 1 :
        print("A judge can give a gymnast %d points." % score)
    else :
        print("A judge can give a gymnast %d point." % score)

#%% Larger Sets

million = list(range(1,1000001))
# print(million)
print("c'est instantané mais ça prend trop de place alors je l'ai mis en commentaire.")

#%% Listing a Sentence

phrase = "Cthulu is awake!"
for lettre in phrase : 
    print(lettre)

#%% List Lengths

numbers = [13,4,27,9,1994]
emplois = ["physician","writer","mangaka","game dev","magician","firefighter"]

cop_num = numbers.copy()
cop_metiers = emplois.copy()

print("il y a " + str(len(cop_num)) + " éléments dans la liste numbers")
print("il y a " + str(len(cop_metiers)) + " carrières dans la liste emplois")

#%% Multiples Of Ten

multipleDix = [num*10 for num in range(1,11)] ; print(multipleDix)

#%% Ordered Numbers 
numbers = [13,4,27,9,1994]

print("Format d'origine \n")
for num in numbers : print(num)

print("\nFormat croissant\n")
c_numbers = numbers.copy()
c_numbers.sort()
for num in c_numbers : print(num)

print("\nFormat d'origine\n")
for num in numbers : print(num)

print("\nFormat décroissant\n")
d_numbers = c_numbers.copy()
d_numbers.reverse()
for num in d_numbers : print(num)

print("\nFormat d'origine\n")
for num in numbers : print(num)

print("\nFormat inversé\n")
r_numbers = numbers.copy()
r_numbers.reverse()
for num in numbers : print(num)

print("\nFormat d'origine\n")
for num in numbers : print(num)

print("\nFormat croissant définitif\n")
numbers.sort()
for num in numbers : print(num)

print("\nFormat décroissant définitif\n")
numbers.reverse()
for num in numbers : print(num)

#%% Ordered Working List

emplois = ["physician","writer","mangaka","game dev","magician","firefighter"]

print("Format d'origine")
for metier in emplois : print (metier)

print("\nFormat alphabétique\n")
a_emplois = emplois.copy()
a_emplois.sort()
for metier in a_emplois : print(metier)

print("\nFormat d'origine\n")
for metier in emplois : print(metier)

print("\nFormat alphabétique inversé\n")
ra_emplois = a_emplois.copy()
ra_emplois.reverse()
for metier in ra_emplois : print(metier)

print("\nFormat d'origine\n")
for metier in emplois : print(metier)

print("\nFormat inversé\n")
r_emplois = emplois.copy()
r_emplois.reverse()
for metier in r_emplois : print(metier)

print("\nFormat d'origine\n")
for metier in emplois : print(metier)

print("\nFormat alphabétique définitif\n")
emplois.sort()
for metier in emplois : print(metier)

print("\nFormat alphabétique inversé définitif\n")
emplois.reverse()
for metier in emplois : print(metier)

#%% Protected List

prenoms = ["Victor","Patrick","Luc"]
c_prenoms = prenoms[:]
c_prenoms.append("Eugene")
c_prenoms.append("François")

print("Origine")
for nom in prenoms : print(nom)
print("")

print("Copie")
for nom in c_prenoms : print(nom)

#%% Starting From Empty

emplois = ["physician","writer","mangaka","game dev","magician","firefighter"]
n_emplois = []
for metier in emplois : n_emplois.append(metier)
print("the first career i thought of was : " + n_emplois[1])
print("the last career i thought was : " + n_emplois[0])

#%% Sentence List

phrase = "Cthulu is awake!"

l_phrase = list(phrase)
print(l_phrase)

#%% Sentence Slices

phrase = "Cthulu is awake!"

print(phrase[:5])
print(phrase[6:11])
print(phrase[-5:])

#%% Working Backwards

tenFirst = []
for i in range(1,11) :
    tenFirst.append(i)

plus_thirteen = []
for i in tenFirst :
    plus_thirteen.append(i + 13)
print(plus_thirteen)

#%% Working List

emplois = ["writer","mangaka","game dev","magician"]
indice = emplois.index("mangaka")
print("magician" in emplois)
emplois.append("firefighter")
emplois.insert(0,"physician")
for metier in emplois : print(" - " + metier)

#%% Your First List

listecourse = ["café","filtre","lait","cacao","sucre"]
print("Oups, j'ai oublié d'acheté du " + listecourse[2] + ".")

#%% Your First list Loop

listecourse = ["café","filtre","lait","cacao","sucre"]
for item in listecourse :
    print( item + ", ça c'est bon.")
