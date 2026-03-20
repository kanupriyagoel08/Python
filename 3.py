p=float(input("Enter the principal amount : "))
r=float(input("Enter rate : "))
t=float(input("Enter time : "))
si=p*(1+(r/100))**t
print(f"{si:.2f}")