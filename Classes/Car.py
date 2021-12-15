class Car :
    def __init__(self,marque="",model="",nbMotrice=2,nbPorte=3,radar=False) :
        self.marque = marque
        self.model = model
        self.nbMotrice = nbMotrice
        self.nbPorte = nbPorte
        self.radar = radar
    
    def description(self) :
        print("%s  |  %s" % (self.marque, self.model))
        print("\t Roues Motrices : %d" % self.nbMotrice)
        print("\t Portes : %d" % self.nbPorte)
        if self.radar :
            print("\t Radar de Recul : oui")
        else :
            print("\t Radar de Recul : non")