def is_year_leap(yr):
    if yr % 4 != 0:
        return False
    elif yr % 100 != 0:
        return True
    elif yr % 400 != 0:
        return False
    else:
        return True

def days_in_month(yr, mo):
    if is_year_leap(yr) and (mo == 2):
        return 29
    result = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    return result[mo]
    

test_years = [1900, 2000, 2016, 1987, 2000]
test_months = [2, 2, 1, 11, 11]
test_results = [28, 29, 31, 30, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
