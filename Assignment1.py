#Calculating Simple Interest

principle = int(input("Enter the principal amount "))
rate = float(input(" Enter the rate of interest  "))
time = int(input( " Enter the number of years "))
simple_interest = (principle * rate * time)/100
print("The simple interest is ",simple_interest)
