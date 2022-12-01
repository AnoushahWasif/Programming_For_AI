class ABC:
    def PQR(self):
        print("1st one")
class DEF:
    def PQR(self):
        print("2nd one")
class XYZ:
    def PQR(self):
        print("3rd one")
a=ABC()
b=DEF()
c=XYZ()

def Print(Toot):
    Toot.PQR()
Print(a)
Print(b)
Print(c)
