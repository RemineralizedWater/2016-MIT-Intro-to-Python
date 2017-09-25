def monthly_int_rate(x):
    return x/12.0


def monthly_unpaid_bal(x, y):
    return x - y


def updated_bal_ea_month(x, y):
    return x + y * x


balance = 999999
annualInterestRate = 0.18

updated_bal = 0.00
unpaid_bal = balance

mon_int_rate = monthly_int_rate(annualInterestRate)

low_bound = balance/12
up_bound = balance * (1 + mon_int_rate)**12/12.0

low_mon_pay = (low_bound+up_bound)/2.0

while unpaid_bal > 0 or unpaid_bal < -0.01:
    updated_bal = balance
    print low_bound
    print up_bound
    print low_mon_pay
    for month in range(1, 13):
        unpaid_bal = monthly_unpaid_bal(updated_bal, low_mon_pay)
        updated_bal = updated_bal_ea_month(unpaid_bal, mon_int_rate)
    if updated_bal > 0:
        low_bound = low_mon_pay
    if updated_bal < 0:
        up_bound = low_mon_pay
    low_mon_pay = (low_bound+up_bound)/2.0
print 'Lowest Payment: ', round(low_mon_pay, 2)