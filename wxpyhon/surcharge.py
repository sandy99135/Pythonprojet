class Vecteur:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self):
        return 'Vecteur (%d, %d)' %(self.x ,self.y)
    def __add__(self,autre):
        return Vecteur(self.x + autre.x,self.y+autre.y)

v1=Vecteur(1,1)
v2=Vecteur(2,2)
print v1

    