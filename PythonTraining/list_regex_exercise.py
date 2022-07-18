import re

List1 = [4,2,6,1,3,8]
List2 = ['Messi', 'Ronaldo', 'Pele', 'Maradona']
List1_1 = []
List2_2 = []

# 1. Sort the list in ascending order and print the first element in the list
List1.sort()
print(List1[0])
List2.sort()
print(List2[0])

# 2. Python program to find the second largest no. in a list
print(List1[1])

# 3. Python program to print odd no.s & even no.s seperately in a list of
#[1,2,3,4,5,6,7,8,9,10]

List3 = [1,2,3,4,5,6,7,8,9,10]
print(List3[::2])
print(List3[1::2])

# 4. program fro reversing a list
print(List3[::-1])

# 5. program to print all odd no.s from 1-50
print(list(range(1,50,2)))

# 6. program to count even and odd no.s in a list
List = [5,2,7,4,9,3]
for i in List:
    if i%2 == 0:
        List1_1.append(i)
    else:
        List2_2.append(i)
print(List1_1)
print(List2_2)


# 1. write a python program to remove zeros from an IP address("216.08.094.196")

ip_addr = "216.08.094.196"
x = re.sub('\.[0]*', '.', ip_addr)
print(x)


# 2. write a python program that matches a string that has an 'a' 
# followed by anything, ending in 'b'

y = 'a.*?b$'

str = 'aabb'
op = re.search(y, str)
print(op)

# 3. replace all occurrences of 6 with 'six' and 10 with 'ten' for the 
# given string 'They ate 6 apples and 10 bananas'

line = 'They ate 6 apples and 10 bananas'
output = re.sub('6','six', line)
output = re.sub('10', 'ten', output)
print(output)
