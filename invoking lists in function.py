def val(lst):
    
    my_list=[]
    counter=0
    
    for elem in lst:
        my_list.append(elem)
        counter+=1
    print('This list has',counter,'no. of elements')
    
    return my_list
    
print("List no.1 is = ",val([10,5,3,8,7]))
print("List no.2 is = ",val([10,5,8,7]))
print("List no.3 is = ",val([3,8,7]))
print("List no.4 is = ",val([10,5]))
