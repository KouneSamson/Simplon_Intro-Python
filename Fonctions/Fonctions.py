#%% Addition Calculator

def additions(x,y) :
    somme = x + y
    print("la resultat de la somme entre %d et %d est %d" % (x,y,somme))
additions(1,1)
additions(2,1)
additions(3,2)

#%% Favorite Colours

def favColours(name,colour) :
    print("%s really like %s" % (name,colour))

favColours("Victor","Red")
favColours("Mélissa","Black")
favColours("Polgara","Blue")

#%% Favorite Movie

def favoriteMovie(movie="The Lord of the Ring") :
    print("%s is one of my favorite movie." % movie)

favoriteMovie("Big Fish")
favoriteMovie()
favoriteMovie("Expelled from Paradise")

#%% Full Names

def fullName(prenom,nom) :
    c_prenom = prenom.capitalize()
    c_nom = nom.upper()
    full = c_prenom + " " + c_nom
    print("Ave, %s !" % full)

prenoms = ["Victor","Mélissa","Polgara"]
nom = "Freyer"
for p in prenoms : fullName(p,nom)

#%% Games

def iLikeGames(name="D&D") :
    print("Playing %s is really fun !" % name)

iLikeGames("Call of Cthulu")
iLikeGames()
iLikeGames("Warhammer")

#%% Greeter

def greetings(name) :
    print("Hello to you, %s" % name)
    print("Everyone has to know that you, %s , are the best" % name)
    print("And we all hope that you, aka %s, are feeling good today!" % name)
prenoms = ["Victor","Mélissa","Polgara"]
for p in prenoms : greetings(p)

#%% Phones

def phoneBrand(brand,model) :
    print("%s %s" % (brand,model))

phoneBrand("Huawei","P30")
phoneBrand("Nokia","3310")
phoneBrand("Samsung","Galaxy S21")

#%% Return Calculator

def alt_additions(x,y) :
    somme = x + y
    return(somme)
b = 3
a = 5
print("la somme entre %d et %d donne %d" % (a,b,alt_additions(a,b)))

#%% Sports Teams

def sportsTeams(ville,team) :
    print("%s de %s" % (team,ville))

sportsTeams(team="Les Dragonnes",ville="Metz")

#%% World Languages

def worldLanguages(langue,pays=None) :
    print("langue : %s" % langue)
    if pays : print("pays : %s" % pays)
    else : print("pays : aucun")

worldLanguages("Français","France")
worldLanguages("Dwarvish")
