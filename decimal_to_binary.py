
def dec_to_bin():
    n=int(input("Enter the number :- "))
    s=""
    while(n>0):
        r=n%2
        s=str(r)+s
        n//=2
    print(s)    
    
    
dec_to_bin()    