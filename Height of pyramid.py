blocks = int(input('Enter the number of blocks ='))
num = 0
n=1
counter = 0

while blocks == 0:
    num = int(input("Please enter the number of blocks = "))
    
while blocks!=0:
    num+=n
    n+=1
    counter+=1
    if blocks<num:
        counter-=1
        break
    
height = counter
print('The height of the pyramid is = ',height)
