# WAP to check a given number is perfect or not (sum of divisor is number itself)

def check_perfect_number(n):
    # n=int(input("Enter the number :- "))
    # r=n
    s=0
    for i in range(1,n):  #  
        if n%i==0:
            s+=i
        else:
            pass
            
    if n==s:
        print("True")   
    else:
        print("False")      
check_perfect_number(28)     