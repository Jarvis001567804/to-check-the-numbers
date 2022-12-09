import random

def status(x,y):
    n = random.randint(x,y)
    print("range is " ,(x,y),"and","randomly picked number is",n)
    print("Then the properties followed by this number are:")
    if n%2==0:
        print(n,"is a even number")
    else:
            print(n,"is a odd number")
    if n>0:
        print(n,"is a positive number")
    else:
        print(n,"is a negative number")
    if n>1:
        for i in range (2,n):
            if (n%i) == 0:
                print(n,"is a composite number")
            else:
                print(n,"is a prime number")
            break
            
status(1,50)
