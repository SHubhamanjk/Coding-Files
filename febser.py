# WAP to generate first n Sequence of Febonacci Series

n=int(input("How Many Sequences you want from febonaccie Series :- "))
a=0
b=1
cnt=2
c=1
print(a,end=" ")
print(b,end=" ")
while(n>cnt):
    c=a+b
    
    cnt+=1
    a=b
    b=c
    print(c,end=" ")