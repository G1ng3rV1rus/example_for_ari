print("Please enter your income for the following months:")
income10 = float(input("October:"))
income11 = float(input("November:"))
income12 = float(input("December:"))
total_income = income10+income11+income12
ave_income = total_income/3
print('Your average monthly income is', ave_income, 'dollar(s)')

print("Now enter your total expenses for the following months:")
exp10 = float(input("October:"))
exp11 = float(input("November:"))
exp12 = float(input("December:"))
total_expense = exp10+exp11+exp12
ave_exp = total_expense/3
print('Your monthly expenses seem to cost you an average of', ave_exp, 'dollar(s)')

print('Your average monthly gain/loss is', ave_income-ave_exp, 'dollar(s)')
