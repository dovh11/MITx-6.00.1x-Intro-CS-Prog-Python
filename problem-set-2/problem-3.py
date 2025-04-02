balance = 320000
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12.0
monthlyPaymentLowerBound = balance / 12
monthlyPaymentUpperBound = (balance * ((1 + monthlyInterestRate)**12)) / 12.0

while True:
    lowestPayment = (monthlyPaymentLowerBound + monthlyPaymentUpperBound) / 2.0
    updatedBalanceEachMonth = balance  # Reset balance at the start of each iteration

    for i in range(12):
        monthlyUnpaidBalance = updatedBalanceEachMonth - lowestPayment
        updatedBalanceEachMonth = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance

    if abs(updatedBalanceEachMonth) < 0.01:  # Check if balance is close to zero
        break
    elif updatedBalanceEachMonth > 0:
        monthlyPaymentLowerBound = lowestPayment
    else:
        monthlyPaymentUpperBound = lowestPayment

print("Lowest Payment: " + str(round(lowestPayment, 2)))