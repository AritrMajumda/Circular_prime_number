n=int(input("enter the number "))
k=n
k1=n
l=n
z=n
s2=-1
a=0
for j in range(1,k1):
    if(k1%j==0):
        a=a+1
    else:
        break
while z>0:
    s1=int(z%10)
    s2=s2+1
    z=int(z/10)
while k>0:
    s=int(k%10)
    p=int((l-s)/10)
    q=int(s*(10**s2)+p)
    q1=q
    for i in range(1,q1):
        if (q%i==0):
            a=a+1
            print(a)
    k==q
    if(a==4):
        print("the number is a circular prime number")
    else:
        print("the number is not a circular prime number")