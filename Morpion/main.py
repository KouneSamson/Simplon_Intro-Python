import sys
import random

class Plateau ():
    
    grille = [['-','-','-'],['-','-','-'],['-','-','-']]
    
    # def __init__(self) :

    def afficher(self):
        for l in self.grille:
            print("| " + l[0] + " | " + l[1] + " | " + l[2] + " |")
        #END for
    #END afficher

    def ligne(self):
        res = False
        for x in range(0,3):
            res = self.grille[x][0] == self.grille[x][1] == self.grille[x][2] != '-'
            if res : break
        return res
    #END ligne
    
    def colonne(self):
        res = False
        for y in range(0,3):
            res = self.grille[0][y] == self.grille[1][y] == self.grille[2][y] != '-'
            if res : break
        return res
    #END colonne
    
    def diagonale(self):
        return ( self.grille[0][0] == self.grille[1][1] == self.grille[2][2] != '-' ) or ( self.grille[0][2] == self.grille[1][1] == self.grille[2][0] != '-' )
    #END diagonale

    def finDeJeu(self):
        return self.ligne() or self.colonne() or self.diagonale()
    #END finDeJeu
#END Plateau


class Jeu():

    plateau = Plateau()
    joueur_actuel = ('X','O')[random.randint(0,1)]
    nb_coups = 0

    def lancement(self):
        rep = input("Voulez vous jouer au Morpion ? (y/n)")
        if rep == ('y') : self.boucleJeu()
        else : print("Aurevoir !"); sys.exit()
    #END lancement

    def afficherGrille(self):
        print("\n____________________________")
        print("Voici l'état actuel du jeu :\n")
        self.plateau.afficher()
    #END afficherGrille

    def jouerUnCoup(self):
        
        print("Joueur " + self.joueur_actuel + " à vous de jouer !")
        
        c = input("Choisir la colone dans laquelle jouer : (0 , 1 , 2)")
        c.strip()
        if c.isdigit(): c = int(c)
        else: c = -1
        
        l = input("Choisir la ligne dans laquelle jouer : (0 , 1 , 2)")
        l.strip()
        if l.isdigit(): l = int(l)
        else: l = -1

        if (0 <= c <=2) and (0 <= l <= 2):
            if self.plateau.grille[l][c] == '-':
                self.plateau.grille[l][c] = self.joueur_actuel
            else:
                print("Ce coup a déjà été joué, en choisir un autre")
                self.jouerUnCoup()
        else:
            print("Ce coup est impossible, en choisir un autre")
            self.jouerUnCoup()
        #END if
    #END jouerUnCoup

    def boucleJeu(self):
        self.afficherGrille()
        self.jouerUnCoup()
        if self.plateau.finDeJeu():
            self.afficherGrille()
            print("Joueur " + self.joueur_actuel + " a gagné la partie")
        elif self.nb_coups >= 8:
            self.afficherGrille()
            print("Match Nul")
        else:
            self.joueur_actuel = ('X','O')[self.joueur_actuel == 'X']
            self.nb_coups += 1
            self.boucleJeu()
        #END if
    #END boucleJeu
#END Jeu

jeu = Jeu()
jeu.lancement()