prenoms = ["Victor","Patrick","Luc"]
c_prenoms = prenoms[:]
c_prenoms.append("Eugene")
c_prenoms.append("François")

print("Origine")
for nom in prenoms : print(nom)
print("")

print("Copie")
for nom in c_prenoms : print(nom)