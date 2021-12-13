famous = ["Poe","Lovecraft","Asimov","Brin"]
famous.pop()
famous.pop(0)
del famous[1]
famous.remove("Lovecraft")
print("il reste " + str(len(famous)) + " célébrité dans la liste famous.")