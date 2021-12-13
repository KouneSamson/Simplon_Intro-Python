emplois = ["writer","mangaka","game dev","magician"]
indice = emplois.index("mangaka")
print("magician" in emplois)
emplois.append("firefighter")
emplois.insert(0,"physician")
for metier in emplois : print(" - " + metier)