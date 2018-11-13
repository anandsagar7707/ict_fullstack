myfile=open("hello.txt","w")
myfile.write("ICTA CALICUT FULLSTACK COURSE")
myfile.close()
print("File generated successfully")

file = open("hello.txt", "r")
print(file.read())
file.close()