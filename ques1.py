#1star pattern  

for i in range(7,0,-1):
    for j in range(1,i):
        print(j,end=" ")
    print()

for x in range(7,0,-1):
    p=1
    for y in range(x,0,-1):
        print(p,end=" ")
        p=p+1
    print()


#2 sum of digits of a number

a=(input("Enter Number: "))
b=len(a)
a=int(a)
sum=0
for i in range(0,b-1):
    sum=sum+(a%10)
    f1=a//10
    a=f1

print(sum+a)


#3 fibonacci series
x=int(input("Enter a number: "))
n1=0

for i in range(0,x):
    for j in range(0,i+1):
        print(x+1)

#To find the number is Armstrong or Not
a=input("Enter Number: ")
b=len(a)
e=int(a)
f=e

sum=0
for i in range(1,b):
    c=e%10
    d=e//10
    sum=sum+c**b
    e=d
sum=sum+e**b
if sum==f:
    print("True")
else:
    print("False")

#Highest Common Factor

a=int(input("Enter Number1: "))
b=int(input("Enter Number2: "))
list1=list()
list2=list()
m=max(a,b)
print(m)
for i in range(1,m+1):
    if a%i==0:
        list1.append(i)
    
for j in range(1,m+1):
    if b%j==0:
        list2.append(j)
print(list1)
print(list2)
common=[]
for x in list1:
    if x in list2:
        common.append(x)
print(max(common))




#Pattern ****
#        *  *
#        *  *
#        ****

s=int(input("Enter Size of Hollow Square: "))
for i in range(s):
    for j in range(s):
        if i==0 or i==s-1 or j==0 or j==s-1:
            print("#",end=" ")
        else:
            print(" ",end=" ")
    print()
