# class Person:
#     def __init__(self,name,age):
#         self.abc=name
#         self.xyz=age
        
# p1=Person("John",36)

# print(p1.xyz)
# print(p1.abc)

class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
        
    def printname(self):
        print(self.firstname,self.lastname)
        
class student(Person):
    def __init__(self, fname,lname,year):
        super().__init__(fname,lname)
        self.graduationyear = year
        
    def print_2(self):
        print(self.firstname,self.lastname,self.graduationyear)
x = student("Paromita","Das","2020")
x.print_2()
