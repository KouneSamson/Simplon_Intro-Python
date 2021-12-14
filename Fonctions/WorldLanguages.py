def worldLanguages(langue,pays=None) :
    print("langue : %s" % langue)
    if pays : print("pays : %s" % pays)
    else : print("pays : aucun")

worldLanguages("Français","France")
worldLanguages("Dwarvish")