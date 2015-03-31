balance=4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
paid=0
for i in range(1,13):
   print("Month: "+str(i))
   mmp=balance*monthlyPaymentRate
   paid+=mmp
   print("Minimum monthly payment: "+str(round(mmp,2)))
   balance=balance-mmp
   balance=balance+balance*annualInterestRate/12
   print("Remaining balance: "+str(round(balance,2)))
   
print("Total paid: "+str(round(paid,2)))
print("Remaining balance: "+str(round(balance,2)))
