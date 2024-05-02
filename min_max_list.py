
# WAP to find max and minimum from the list of intergers

def find_min_max():
    n=int(input("How Many Elements , you wanna see in list : "))
    l=[]
    for i in range(0,n):
        a=int(input(f"Enter the {i+1} element : "))
        l.append(a)
    def find_max(l):
        mx=l[0]

        for i in range(0,len(l)):
            if mx<l[i]:
                mx=l[i]
            else:
                continue 
        return mx 
        
    def find_min(l):
        mn=l[0]

        for i in range(0,len(l)):
            if mn>l[i]:
                mn=l[i]
            else:
                continue 
        return mn
    print("Maximum value in the list:", find_max(l))
    print("Minimum value in the list:", find_min(l))
find_min_max()      