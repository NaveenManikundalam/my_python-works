c0=int(input("Enter a the number = "))

while c0<=0:
    c0=int(input("Please enter a non-negative and non-zero number = "))

steps =0

if c0>0:
    while c0!=1:
        if c0 % 2 == 0:
            c0//=2
            print(c0)
        else:
            c0=3*c0+1
            print(c0)
        steps+=1

print("Steps =",steps)
            
