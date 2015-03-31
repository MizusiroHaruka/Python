balance = 999999
annualInterestRate = 0.18
q=1+annualInterestRate/12
Low=((q**11*(1-q))/(1-q**12))*balance
print("Lowest Payment: "+str(round(Low,2)))
