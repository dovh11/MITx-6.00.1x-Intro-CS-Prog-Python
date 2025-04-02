balance = 3926
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12.0
updatedBalanceEachMonth = balance
minimumFixedMonthlyPayment = 0

while updatedBalanceEachMonth > 0:
    updatedBalanceEachMonth = balance
    minimumFixedMonthlyPayment += 10

    for i in range(12):
        monthlyUnpaidBalance = updatedBalanceEachMonth - minimumFixedMonthlyPayment
        updatedBalanceEachMonth = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance

print("Lowest Payment: " + str(minimumFixedMonthlyPayment))