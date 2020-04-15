for t in range(int(input())):
    income = int(input())
    tax = 0
    if(income <= 250000):
        tax = 0
    elif 250000 <= income <= 500000:
        tax = 0.05 * (income - 250000)
    elif 500000 <= income <= 750000:
        tax=12500 + 0.10 * (income - 500000)
    elif 750000 <= income <= 1000000:
        tax=37500 + 0.15 * (income - 750000)
    elif 1000000 <= income <= 1250000:
        tax=75000 + 0.20 * (income - 1000000)
    elif 1250000 <= income <= 1500000:
        tax=125000 + 0.25 * (income - 1250000)
    else:
        tax=187500 + 0.30 * (income - 1500000)
    print(int(income-tax))