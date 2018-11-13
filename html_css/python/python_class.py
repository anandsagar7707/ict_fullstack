# class Students:
#     name="Mahesh"
#     rollno=2

#     def getAge(self,myAge):
#          print('Age is '+str(myAge))

    
# s=Students()
# x=int(input("enter the age"))
# (s.getAge(x))



# # print(s.name)
# # print(s.getAge())
# # print(s.rollno)

class Students:
    def __init__(self,x,y):  #init is a special character
        self.name=x
        self.rollno=y

    def printData(self):
        print("Name ="+ str(self.name))
        print("RollNo ="+str(self.rollno))

    def getAge(self,myAge):
        print('Age is '+str(myAge))
s=Students("Rahul R",1)

x=int(input("Enter the age"))

s.printData()
s.getAge(x)