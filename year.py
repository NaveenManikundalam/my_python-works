year = int(input("Enter a year: "))

if year <=1580:
    print('Not within the Gregorian calendar period')
    
elif (year % 4 !=0) and (year % 400 !=0):
    print("Common year")

elif year % 100 !=0:
    print("Leap Year")

else:
    print("Leap Year")

    
    
