class Complex:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self,complex):
        return Complex(self.x+complex.x,self.y+complex.y)
    def multiply(self,complex):
        return Complex(self.x*complex.x-self.y*complex.y,self.x*complex.y+self.y*complex.x)
    def modulus(self):
        return (self.x**2 + self.y**2)**(1/2)
    def conjugate(self):
        return Complex(self.x,-self.y)
    def inverse(self):
        return Complex(self.x/(self.modulus()**2),self.y/(self.modulus()**2))
c1=Complex(1,2)
# c2=c1.inverse()

# print(c1.x, c1.y)
# print(c2.x, c2.y)
print(c1.inverse())
    
    