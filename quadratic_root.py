# WAP to find root of a quaratic equation

def root_finder():
    print("Format of a quadratic equation is ---> ax^2+bx+c")
    print()
    a=int(input("Enter the value of a :- "))
    b=int(input("Enter the value of b :- "))
    c=int(input("Enter the value of c :- "))

    x1=(-b+((b**2-4*a*c))**1/2)/2*a
    x2=(-b-((b**2-4*a*c))**1/2)/2*a

    print(f"Roots of equation are ---> {x1} , {x2}")
