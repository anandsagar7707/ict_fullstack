# def display():
#     print("Welcome to python")

# display()



# def add(x,y):
#     z=x+y
#     print(z)
# def sub(x,y):
#     z=x-y
#     print(z)
# def div(x,y):
#     z=x/y
#     print(z)
# def mul(x,y):
#     z=x*y
#     print(z)

# x = int(input("Enter Num1:"))
# y = int(input("Enter Num 2:"))

# add(x,y)
# sub(x,y)
# mul(x,y)
# div(x,y)




# def add(x,y):
#     z=x+y
#     return z
# def sub(x,y):
#     z=x-y
#     return z
# def div(x,y):
#     z=x/y
#     return z
# def mul(x,y):
#     z=x*y
#     return z

# x = int(input("Enter Num1:"))
# y = int(input("Enter Num 2:"))

# result=add(x,y)
# print(result)
# result=sub(x,y)
# print(result)
# result=mul(x,y)
# print(result)
# result=div(x,y)
# print(result)


def large(x,y,z):
    if(x>y):
        if(x>z):
            return x
        else:
            return z
    else:
        if(y>z):
            return y
        else:
            return z



a = int(input("Enter Num1: "))
b = int(input('Enter Num2: '))
c = int(input("Enter Num3: "))

largest = large(a,b,c)
print("Largest number is"+"  "+str(largest))
