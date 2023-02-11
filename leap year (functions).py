def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

test_data = [1900, 2000, 2016, 1987,2005]
test_results = [False, True, True, False, True]


for i in range(len(test_data)):
	year = test_data[i]
	print(year,"->",end="")
	result = is_year_leap(year)
	if result == test_results[i]:
		print("Correct")
	else:
		print("Failed")
