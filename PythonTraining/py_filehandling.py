#File handling

#trying to open a file myfile.txt in the same dir
#using open() method get the file object

myFile = open("myfile.txt", "r")
 
#to read the contents, use the read() method

#print(myFile.read(10))
print(myFile.readline())
print(myFile.readline())
print(myFile.readline())