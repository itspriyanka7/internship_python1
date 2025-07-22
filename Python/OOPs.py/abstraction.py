from abc import ABC,abstractmethod

class manasvi(ABC):
    def __init__(self,name,address):
     self.name=name
     self.address=address
    @abstractmethod
    def std(self):
        pass 
    def piyush(self):
       print("welcome")
       

class srushti(manasvi):
    def __init__(self, name, address, id ):
       super().__init__(name, address)
       self.id=id

    def std(self):
        print("hello world")

m=srushti("Priyanka","nashik",101)
print(m.name)
print(m.address)
print(m.id)
        
    
