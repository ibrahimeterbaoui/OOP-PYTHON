class Module:

    __nom = 0
    __volume_horaire = 0
    __semestre = ""
    ListMatiere = []
    def __init__(self, nom="", volume_horaire=0, semestre=""):
        self.__nom = nom
        self.__volume_horaire = volume_horaire
        self.__semestre = semestre

    def display(self):
        print(self.__nom,  self.__volume_horaire, self.__semestre)
class Matiere:

    __nom = 0
    __pourcentage = 0
    module = Module()
    ListeAnnesAcademique = []
    def __init__(self, nom="", pourcentage=0):
        self.__nom = nom
        self.__pourcentage = pourcentage

    def display(self):
        print(self.__nom, self.__pourcentage)

class Utilisateur:

    _nom = ""
    _email = ""
    _mot_de_passe = ""
    _genre = ""
    _age = 0

    def __init__(self, nom="", email="", mot_de_passe="", genre="", age=0):
        self._nom = nom
        self._email = email
        self._mot_de_passe = mot_de_passe
        self._genre = genre
        self._age = age

    def display(self):
        print(self._nom, self._email, self._mot_de_passe,  self._genre,  self._age)


class Professeur(Utilisateur):

    __ppr = 0
    __grade = ""
    module = Module()
    ListeMatieres = []
    ListeAnnesAcademique = []

    def __init__(self, nom="", email="", mot_de_passe="", genre="", age=0, ppr=0, grade=""):
        super().__init__(self, nom, email, mot_de_passe, genre, age)
        self.__ppr = ppr
        self.__grade = grade

    def display(self):
        print(self.__ppr, self.__grade)


class Annee_Academique:

    __anne = ""
    Listetudiant = []
    Listematiesre = []
    Listeprofesseur = []

    def __init__(self, anne=""):
        self.__anne = anne

    def display(self):
        print(self.__anne)


class Etudiant(Utilisateur):

    __code_massar = ""
    ListAnneAcademique = []

    def __init__(self, nom="", email="", mot_de_passe="", genre="", age=0, code_massar=""):
        super().__init__(nom, email, mot_de_passe, genre, age)
        self.__code_massar = code_massar

    def display(self):
        print(self.__code_massar)

