balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate / 12.0
updatedBalanceEachMonth = balance

for i in range(12):
    minimumMonthlyPayment = monthlyPaymentRate * updatedBalanceEachMonth
    MonthlyUnpaidBalance = updatedBalanceEachMonth - minimumMonthlyPayment
    updatedBalanceEachMonth = MonthlyUnpaidBalance + (monthlyInterestRate * MonthlyUnpaidBalance)

remainingBalance = round(updatedBalanceEachMonth, 2)
print("Remaining balance: " + str(remainingBalance))
    