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