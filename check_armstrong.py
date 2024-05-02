#  WAP to check given number is armstrong or not

n=int(input("Enter the number:-  "))
t=n
t1=n
cnt=0
res=0
while(t>0):
    t=t//10
    cnt+=1

while(t1>0):
    r=t1%10
    res+=r**cnt
    t1//=10
   
if res==n:
    print("True")    
else:
    print("False")   