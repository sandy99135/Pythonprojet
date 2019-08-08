class Personne:
    def __init__(self, nom,age):
        self.nom = nom
        self.age = age
        self.prenom = "Martin"
    def strs(self):
        return "{0} {1}".format(self.prenom, self.age, self.nom)

class AgentSpecial(Personne):
    def __init__(self, nom,age, matricule):
        # On appelle explicitement le constructeur de Personne :
        Personne.__init__(self, nom,age)
        self.matricule = matricule
    def strs(self):
        return self.nom,self.prenom,self.age,self.matricule

agent = AgentSpecial("Fisher","2", "18327-121")
print agent.strs()