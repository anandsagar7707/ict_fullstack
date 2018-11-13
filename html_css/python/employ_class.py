class Employee:
    def __init__(self,w,x,y,z):
        self.name=w
        self.age=x
        self.salary=y
        self.code=z
    def printdata(self):
        print("employee name :",self.name)
        print("employee age :",self.age)
        print("employee.salary :",self.salary)
        print("employee.code :",self.code)

n=input("enter the name :")
a=int(input("enter age  :"))
s=int(input("enter the salary :"))
c=int(input("enter the cod :"))

e=Employee(n,a,s,c)
e.printdata()