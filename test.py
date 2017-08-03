x = 100000
xx = str(x)

list1 = []
list2 = []
zero_flag =True
#
# if xx[0] == "-":

for i in range(len(xx)-1):
    list1.append(xx[i+1])
for j in range(len(xx)-1):
    list2.append(list1.pop(j))

print list2
m=0
while list2[m]==0:
    list2.pop(m)
    m=m+1

list2.insert(0,"-")
print list2

mystring = ""
for i in range(len(xx)):
    mystring = mystring + list2[i]


print mystring

