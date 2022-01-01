class  Vecteur2D:
   x=0
   y=0
   
   def __init__(self, x=0, y=0):
      self.x = x
      self.y = y
      self.s = self.x+self.y
   def display(self):
      print("x= %d y= %d la somme est %d " %( self.x , self.y , self.s))

class Rectangle:
   
    def __init__(self, longueur=15, largeur=10):   
        self.long = longueur                           #Initialisation avec valeurs par defaut
        self.larg = largeur
        self.nom = "rectangle"
    def surface(self):    
        return (self.long * self.larg)                          #Retourne la surface du rectangle 
    def display(self):    # Affichage des informations du rectangle.
       print ("la surface du {0} de cote {1} et {2} est : {3}".format(self.nom, self.long, self.larg, self.surface()))

 
class Carre(Rectangle):                #classe carre fille de la class Rectangle
   

    def __init__(self, cote=8):
        Rectangle.__init__(self, cote, cote)  #Constructeur avec valeur par defaut
        self.nom = "carre" 

class Point:                   #classe des points du plan

    
    def __init__(self, x=0.0, y=0.0):    
        self.px = float(x)                        #Initialisation avec valeurs par defaut
        self.py = float(y)

class Segment:                                  #classe segment utilisant la classe Point
   
    def __init__(self, x1, y1, x2, y2):
        self.orig = Point(x1, y1)               #L'initialisation deux pour l’origine et deux pour l’extremite.
        self.extrem = Point(x2, y2)
    def display(self):        #Representation d'un objet segment
        print ("le segment: [({0}, {1}),({2}, {3})]".format(self.orig.px, self.orig.py, self.extrem.px, self.extrem.py))

v1 = Vecteur2D(2,101)
v2 = Vecteur2D(7,102)
v1.display()
v2.display()
print("**********************************************************")
r1 = Rectangle()
r2 = Rectangle(10, 6)
c1 = Carre()
c2 = Carre(7)
print("Carre :  \n")
r1.display() 
print("  sans parametre \n")
r2.display()
print("  avec parametre \n")

print("**********************************************************")
s = Segment(1, 2, 3, 4)
s.display()
print("\n \n ")