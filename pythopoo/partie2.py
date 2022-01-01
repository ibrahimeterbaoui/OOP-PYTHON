class Etudiant:

    nom = ""
    prenom = ""
    age = 0
    cne = ""
    moyenne = 0

    def __init__(self, nom="", prenom="", age=0, cne="", moyenne=0):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.cne = cne
        self.moyenne = moyenne
    def display(self):
        print("[",self.nom, "]","[", self.prenom, "]", "[",self.age, "]", "[", self.cne, "]", "[",self.moyenne , "]")


e1 = Etudiant("nom 1", "prenom 1", 19, "p23102001", 20)
e2 = Etudiant("nom 2", "prenom 2", 10, "p23102001", 15)
e3 = Etudiant("nom 3", "prenom 3", 7, "p23102001", 5)
e4 = Etudiant("nom 4", "prenom 4", 12, "p23102001", 14)
e5 = Etudiant("nom 5", "prenom 5", 17, "p23102001", 16)

ListEtudiants = []
ListEtudiants.append(e1)
ListEtudiants.append(e2)
ListEtudiants.append(e3)
ListEtudiants.append(e4)
ListEtudiants.append(e5)

#ordre selon l'age et la moyen :

def MySort1(etudiant):
    return -etudiant.moyenne - etudiant.age

# affichage par ordre selon l'age et la moyen :
ListEtudiants.sort(key=MySort1)
for i in ListEtudiants:
    i.display()

