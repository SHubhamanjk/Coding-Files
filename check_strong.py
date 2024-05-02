# WAP to check a given number is strong number or not (sum of factorial of each digit is number itself )
 
 
def check_strong_number(n):    
# n=int(input("Enter the number :- "))  

    def find_fact(n):
        if n==0:
            return 1
        else:
            return n*find_fact(n-1) 
        
    r=n
    s=0
    while(r>0):
        c=r%10
        s+=find_fact(c)
        r//=10

    if n==s:
        print("True")   
    else:
        print("False")    
        
check_strong_number(145)