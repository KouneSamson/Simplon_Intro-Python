def fullName(prenom,nom) :
    c_prenom = prenom.capitalize()
    c_nom = nom.upper()
    full = c_prenom + " " + c_nom
    print("Ave, %s !" % full)

prenoms = ["Victor","Mélissa","Polgara"]
nom = "Freyer"
for p in prenoms : fullName(p,nom)