number_of_days = int(input("Enter numbers of days: "))
number_of_yers = number_of_days//365
number_of_months =  (number_of_days % 365) // 30 
number_of_weeks = (number_of_days % 365) % 30 / 7
remaining_number_of_days = number_of_days % 365 % 7

print(f"Yers: {number_of_yers}, Months: {number_of_months}, Weeks: {number_of_weeks}, Days: {remaining_number_of_days}")