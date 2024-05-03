
def bin_to_dec():
    n=int(input("Enter the Binary Code :- "))
    d=0
    count=0
    s=n
    while(s>0):
        r=n%10
        count+=1
        s//=10
        
    for i in range(0,count):
        e=n%10
        d+=e*(2**i) 
        n//=10
    print(d)    
    
bin_to_dec()    
    