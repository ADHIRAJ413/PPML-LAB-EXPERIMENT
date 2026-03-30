principal=float(input("enter principal amount:"))
time=float(input("enter time in years:"))
rate=float(input("enter rate of interest:"))
simple_interest=(principal*time*rate)/100
compound_amount=(principal*(1+rate/100)**time)
compound_interest=compound_amount-principal
print(f"simple interest",simple_interest)
print(f"compound amount",compound_amount)
print(f"compound interest",compound_interest)