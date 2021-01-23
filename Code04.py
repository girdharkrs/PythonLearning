name = input ("enter student's name : " )

print (name)

x = int(input("enter marks in maths out of 100: "))

print (x)

y = int(input(" enter marks in science out of 100 : "))

print (y)

a = int (input("enter marks in English out of 100: "))

print  (a)

b = int (input("enter marks in Hindi out of 100: "))

print  (b)

e = int (input(" enter marks in SST out of 100: "))

z=(x+y+a+b+e)/5

print("average marks are : ",z)

if z > 90 :
    print ( name , " got A grade" )
elif z > 80 :
    print ( name , " got B grade" )
elif z > 70 :
    print ( name , " got C grade" )
elif z > 60 :
    print ( name , " got D grade" )
elif z > 33 :
    print ( name , " got E grade" )
else  :
    print ( name , " FAILED" )
