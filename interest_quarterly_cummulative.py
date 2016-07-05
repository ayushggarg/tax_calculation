import math

def roundoff (value):
    if (value * 10 - (int(value) * 10) < 5):
        return (math.floor(value))
    else:
        return (math.ceil(value))

principle = int(input("\nPrinciple: "))
rate = float(input("Rate: "))
time = int(input("Time (3/6/9/12): "))
months = int(input("Months: "))
print ("")

counter = time
amount = principle
interest_total = 0
tax_total = 0

while (counter <= months):
    interest = float(rate * amount * time / 1200)
    interest = roundoff(interest)
    interest_total += interest
    tax = float(0.1 * interest)
    tax = roundoff(tax)
    tax_total += tax
    amount = (interest - tax + amount) 
    counter += time 
    print (interest, tax, interest-tax, amount)
print (interest_total, tax_total, interest_total-tax_total)
print ("")