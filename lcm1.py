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

g=gcd(x,y)
print(int(g*(x/g)*(y/g)))