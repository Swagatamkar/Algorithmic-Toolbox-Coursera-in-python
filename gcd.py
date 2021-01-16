def gcd(a,b):
    if b==0:
        return a
    else:
        a=a%b
        return gcd(b,a)
#x=int(input("Enter the  first number"))
#y=int(input("Enter the second number"))
x,y=input().split()
x=int(x)
y=int(y)

print(gcd(x,y))