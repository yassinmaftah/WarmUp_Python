from abc import ABC, abstractmethod
from datetime import date

# Abstract Base Classes
class Employe(ABC):
    def __init__(self, nom, matricule, prenom, annee_naissance):
        self.nom = nom
        self.matricule = matricule
        self.prenom = prenom
        self.annee_naissance = annee_naissance

    def __str__(self):
        return f"Matricule: {self.matricule} | Nom: {self.nom} {self.prenom} | annee_naissance: {self.annee_naissance}"

    @abstractmethod
    def get_salaire(self):
        pass



class Ouvrier(Employe) :
    SMIG = 2500
    def __init__(self, nom, matricule, prenom, annee_naissance,annee_entree):
        super().__init__(nom, matricule, prenom, annee_naissance)
        self.annee_entree = annee_entree
    def __str__(self):
        return f"Matricule: {self.matricule}\n\
        | Nom: {self.nom} {self.prenom} |  \n\
        | annee_entree : {self.annee_entree} \n\
        annee_naissance: {self.annee_naissance}\n"

    def get_salaire(self):
        return min(self.SMIG + ((date.today().year - self.annee_entree) * 100), self.SMIG * 2)


class Cadre(Employe) :
    def __init__(self, nom, matricule, prenom, annee_naissance,indice):
        super().__init__(nom, matricule, prenom, annee_naissance)
        self.indice = indice

    def __str__(self):
        return f"Matricule: {self.matricule}\n\
        | Nom: {self.nom} {self.prenom} |\n\
        indice : {self.indice}\n"


    def get_salaire(self):
        if self.indice == 1 :
            return 13000
        elif self.indice == 2:
            return 15000
        elif self.indice == 3:
            return 17000

        
class Patron(Employe):
    chiffre_affaire = 5000000
    def __init__(self, nom, matricule, prenom, annee_naissance):
        super().__init__(nom, matricule, prenom, annee_naissance)

    def __str__(self):
        return f"Matricule: {self.matricule}\n\
        | Nom: {self.nom} {self.prenom} |  \n\
        annee_naissance: {self.annee_naissance}\n"

    def get_salaire(self):
        return self.chiffre_affaire * 0.1



O =  Ouvrier("Yassine",1234,"Maftah",2004,2020)
C =  Cadre("Amine",4321,"elhailaa",2002,2)
P =  Patron("hamid",3456,"hamid-2",1992)

print(O)
print(O.get_salaire())

print(C)
print(C.get_salaire())

print(P)
print(P.get_salaire())


print("#" * 50)


class Ir():
    _tranches = [0, 28000, 40000, 50000, 60000, 150000]
    _taux_ir = [0.0, 0.12, 0.24, 0.34, 0.38, 0.40]

    @staticmethod
    def get_ir(salaire_annuel) :
        for i in range(len(Ir._tranches) - 1, -1, -1):
            if salaire_annuel >= Ir._tranches[i]:
                return Ir._taux_ir[i]
        return 0.0


class IEmploye(ABC):
    def __init__(self,mtle,nom,date_naissance,date_embauche,salaire_base):
        self.mtle = mtle
        self.nom = nom
        self.date_naissance = date_naissance
        self.date_embauche = date_embauche
        self.salaire_base = salaire_base
    
    @abstractmethod
    def age():
        pass
    @abstractmethod
    def anciennete():
        # le nombre d'années travaillées
        pass

    @abstractmethod
    def date_retraite(age_retraite):
        # date de retraite = date de naissance + âge de retraite
        pass

class Employe(IEmploye):

    def __init__(self,mtle,nom,date_naissance,date_embauche,salaire_base):
        super().__init__(mtle,nom,date_naissance,date_embauche,salaire_base)

    def age(self):
        return date.today().year - self.date_naissance.year

    def anciennete(self):
        return date.today().year - self.date_embauche.year

    def date_retraite(self, age_retraite):
        return self.date_naissance.year + age_retraite

    @abstractmethod
    def salaire_a_payer() :
        #  le salaire net d'un employé
        pass

    def __str__(self):
        return f"\
        mtle : {self.mtle}\n\
        nom : {self.nom}\n\
        date_naissance : {self.date_naissance}\n\
        date_embauche : {self.date_embauche}\n\
        salaire_base : {self.salaire_base}\n"


class Formateur(Employe):
    remuneration_hsup = 70
    def __init__(self, mtle, nom, date_naissance, \
                date_embauche, salaire_base,heure_sup):
        super().__init__(mtle, nom, date_naissance, date_embauche, salaire_base)
        self.heure_sup = heure_sup

    def get_remuneration_hsup(self) :
        return self.remuneration_hsup

    def salaire_a_payer(self) :
    # Salaire net = (salaire_base + heure_sup × remuneration_hsup) × (1 − taux IR)
        return (self.salaire_base + self.heure_sup * self.remuneration_hsup) *\
        (1 - Ir.get_ir(self.salaire_base * 12))



f = Formateur("YSN-33","Yassine",date(2004, 6, 29),date(2024, 6, 29),6000,12)
print(f)
print(f"Age: {f.age()} ans")
print(f"anciennete: {f.anciennete()} ans")
print(f"salaire_a_payer : {f.salaire_a_payer()} DH")