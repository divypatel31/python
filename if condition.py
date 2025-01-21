#1
a=int(input("enter the number"))
b=int(input("enter the number"))

if a>b:
    print("a is largest",a)
elif a==b:
    print(a,"=",b)
else:
    print("b is largest",b)

#2
a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))

if a>b and a>c:
    print("a is largest",a)
elif b>a and b>c:
    print("b is largest",b)
elif a==b and b==c and a==c:
    print(a,"=",b,"=",c)
else:
    print("c is largest",c)

#3
a=int(input("enter the number"))

if a%2==0:
    print(a,"the number is even")
else:
    print(a,"the number is odd")

#4
a=int(input("enter the number"))

if a%10==0:
    print(a,"the number is divisible by 10")
else:
    print(a,"the number is not divisible by 10")

#5
a=int(input("enter the number"))
if a<18:
    print(a,"person  minor")
else:
    print(a,"person  major")

#6
a=input("enter the number")
b=len(a)
print("no. of digits is",len(a))

#7
a=int(input("enter the number"))

if a%400=!0 or a%4==0 and a%100==0:
    print("this",a," is  leap year")
else:
    print("this",a," is not leap year")

#8
a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))

if a+b+c==180:
    print("exist triangl")
else:
    print("not exist triangle")

#9
a=int(input("enter the number"))

if a<0:
    print(abs(a))
else:
    print(a)

#10
a=int(input("enter the number"))
b=int(input("enter the number"))
area=a*b
perimter=a+b

if area>perimter:
    print(area,">=",perimter)
elif area==perimter:
    print(area,"=",perimter)
else:
      print(area,"<=",perimter)

#11
def num(x1,y1,x2,y2,x3,y3):
    
    area=0.5*abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))

    return area==0
x1,y1=int(input("enter the number")) , int(input("enter the number"))
x2,y2=int(input("enter the number")) , int(input("enter the number"))
x3,y3=int(input("enter the number")) , int(input("enter the number"))

if  num(x1,y1,x2,y2,x3,y3):
    print("the point are coolinear")
else:
    print("the point are not coolinear")

#12
