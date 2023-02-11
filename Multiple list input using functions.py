counter=0

lists=int(input('Enter the number of lists needed = '))

def message():
    my_list=[]
    for i in range(length):
        val=int(input('Enter the values of the list = '))
        my_list.append(val)
    print('The list no.',counter,'is =',my_list)
    print('We end here')
    del my_list
        
for i in range(lists):
    length=int(input("\nPlease enter the length of the list ="))
    print("We start here !!")
    counter+=1
    message()

print('Thank you very much!!!')

