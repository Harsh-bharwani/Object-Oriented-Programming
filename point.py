import math
class point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def unit(self):
        return (self.x/self.distance_from_origin(),self.y/self.distance_from_origin(),self.z/self.distance_from_origin())
    def distance_from_origin(self):
        return (self.x**2 + self.y**2 + self.z**2)**(1/2)
    def distance(self,p):
        return point(self.x-p.x,self.y-p.y,self.z-p.z).distance_from_origin()
    def is_equal(self,p):
        if(self.x==p.x and self.y==p.y and self.z==p.z):
            return "Yes"
        else:
            return "No"
    def cross_product(self,p):
        li=[]
        li.append(self.y*p.z-p.y*self.z)
        li.append(self.x*p.z-p.x*self.z)
        li.append(self.x*p.y-p.x*self.y)
        return li
    def dot_product(self,p):
        return self.x*p.x +self.y*p.y + self.z*p.z
    def rotate(self,angle):
        li=[]
        radian=math.radians(angle)
        li.append(self.x*math.cos(angle)-self.y*math.sin(angle))
        li.append(self.x*math.sin(angle)+self.y*math.cos(angle))
        return li 
    def print(self):
        print(f'x:{self.x},y:{self.y},z:{self.z}')
p1=point(1,2,1)
p2=point(0,1,0)
p1.print()
print(p1.unit())
# print(p1.cross_product(p2))
# print(p1.dot_product(p2))
# print(p1.is_equal(p2))
# print(p1.distance(p2))
# print(p1.distance_from_origin())
print(p1.unit())
# print(p1.rotate(30))

