def monthly_int_rate(x):
    return x/12.0


def monthly_unpaid_bal(x, y):
    return x - y


def updated_bal_ea_month(x, y):
    return x + y * x


balance = 4739828
annualInterestRate = 0.2

low_mon_pay = 0.00
updated_bal = balance

mon_int_rate = monthly_int_rate(annualInterestRate)

while updated_bal > 0:
    updated_bal = balance
    low_mon_pay += 10.00
    print low_mon_pay
    for month in range(1, 13):
        unpaid_bal = monthly_unpaid_bal(updated_bal, low_mon_pay)
        updated_bal = updated_bal_ea_month(unpaid_bal, mon_int_rate)
print 'Lowest Payment: ', int(low_mon_pay)