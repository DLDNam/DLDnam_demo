def UCLN(a,b):
    i=a
    while a%i !=0 or b % i != 0:
        i=i-1
    return i

class Phanso:
    def __init__(self,ts,ms):
        self.TUSO = ts
        self.MAUSO = ms
        self.KTra = True
        if self.MAUSO == 0:
            self.KTra = False
    def in_Phanso(self):
        if self.KTra == False:
            print("Mau so khong phu hop")
            return
        print(self.TUSO,'/',self.MAUSO)
    def rutgon(self):
        if self.KTra == False:
            return
        x=UCLN(self.TUSO,self.MAUSO)
        self.TUSO = self.TUSO // x
        self.MAUSO = self.MAUSO // x 
a = int(input())
b = int(input())      
p1=Phanso(a,b)
p1.in_Phanso()
p1.rutgon()
if b!=0:
    p1.in_Phanso()

