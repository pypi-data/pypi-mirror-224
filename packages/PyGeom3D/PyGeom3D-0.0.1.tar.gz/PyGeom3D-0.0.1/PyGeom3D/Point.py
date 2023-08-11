import math
class Point:
    def __init__(self,xyz):
        
        self.x=xyz[0]
        self.y=xyz[1]
        self.z=xyz[2]
    def dot(self,other):
        return self.x*other.x+self.y*other.y+self.z*other.z
    
    def __sub__(self,other):
        return Point([self.x-other.x,self.y-other.y,self.z-other.z])
    
    def distance(self,other):
        return math.sqrt((self.x-other.x)**2+(self.y-other.y)**2+(self.z-other.z)**2)
    
    def cross(self,other):
        return Point([self.y*other.z-self.z*other.y,
                     self.z*other.x-self.x*other.z,
                     self.x*other.y-self.y*other.x])
    def __repr__(self):
        return f"({self.x},{self.y},{self.z})"
    

