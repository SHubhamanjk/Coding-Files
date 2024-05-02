# WAP to find Sum Of Digit Of A Number

n=int(input("Enter the number :- "))
s=0
while(n>0):
    r=n%10
    s+=r
    n//=10
print(s)    