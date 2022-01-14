#var #5
from random import *
#1
print("vvedite skolko vi hotite postroit domov = ")
k =  ["  ~~~~~  ",
      " /_____\ ",
      " | []  | ",
      "  -----  " ]
n=int(input())
for i in k:
    print(i*n)
#4
s=0
for i in range (0,13,1):
    print("Plotnost naseleniya =", i)
    p=randint(1,20)
    square=randint(10,50)
    s=0
    s+=p/square
    print("km2:",round(s,1))
#5
for i in range(1, 11, 1):
   y = -0.5*i + i
   print("x= ",i,"; y=",y)
#2

a=20
b=20
klass1=20
klass2=20
sred1=0
while b>=0:
    b-=1
    rand=randint(1,5)
    sred1+=rand
sred1=sred1/klass1
print("Srednyaya ocenka v klasse 1 =  ", sred1)
sred2=0
while a>=0:
    a-=1
    rand=randint(1,5)
    sred2+=rand
sred2=sred2/klass2
print("Srednyaya ocenka v klasse 1 =  ", sred2)

#3
a=0
b=2.0
c=randint(20,30)
while c>0:
    c-=1
    d=uniform(1.0,5.0)
    if a<d:
        a=0
        a+=d
    if b>d:
        b=0
        b+=d
print("Samiy visokiy ball =  ", round(a,1))
print("Samiy nizkiy ball =  ", round(b,1))