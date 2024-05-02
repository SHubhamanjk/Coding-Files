# WAP to generate prime number between 1 to n
    
def isprime(n):
    if n<2:
        return 0
    elif n==2:
        return 1
    else:
        for i in range(2,n):
            if n%i==0:
                return 0
                break
        else:
            return 1
            # break
n=int(input("Enter the number :- "))
for i in range(n+1):
    if isprime(i)==1:
        print(i,end=" ")
    else:
        pass    