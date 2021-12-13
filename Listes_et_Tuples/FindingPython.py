monty = "Le langage Python porte son nom en l'honneur de la troupe des Monty Python"
print("Python" in monty)
print(monty.find("Python"))
print(monty.rfind("Python"))
print(monty.count("Python"))
montyspliton = monty.split()
print(montyspliton)
for mot in montyspliton : print(mot)
print(monty.replace("Python","Ruby"))