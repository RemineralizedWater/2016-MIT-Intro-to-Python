def monthly_int_rate(x):
    return x/12.0


def min_monthly_pay(x, y):
    return x * y


def monthly_unpaid_bal(x, y):
    return x - y


def updated_bal_ea_month(x, y):
    return x + y * x


balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

total_paid = 0.00
total_int_to_date = 0.00

mon_int_rate = monthly_int_rate(annualInterestRate)

for month in range(1, 13):
    min_mon_pay = min_monthly_pay(monthlyPaymentRate, balance)
    unpaid_bal = monthly_unpaid_bal(balance, min_mon_pay)
    balance = updated_bal_ea_month(unpaid_bal, mon_int_rate)

    total_paid += min_mon_pay
    total_int_to_date += mon_int_rate * unpaid_bal

    print 'Month: ', month
    print 'Minimum monthly payment:', round(min_mon_pay, 2)
    print 'Remaining balance:', round(balance, 2)


print 'Total paid: ', round(total_paid, 2)
print 'Remaining balance: ', round(balance, 2)
print 'Total debt accrued due to interest: ', round(total_int_to_date, 2)