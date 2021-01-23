## Fibonacci numbers

name = input ("Enter your Name : " )

print (name)

x = int(input(" \n Enter how many fibonacci numbers you want: "))

print (x)

f1 = 0

f2 = 1

print(" \n Fibonacci Numbers are as below : ", "Total numbers : ", x)

if x >= 1 :
    print (f1, "  ")

if x >= 2 :
    print (f2, "  ")

for n in range(3,x+1) :
    sum = f2 + f1
    print (sum, "  ")
    a = f2
    f2 = sum
    f1 = a
    

    
    
    
