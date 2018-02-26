print("A Program to calculate simple interest")
p = input("Enter principle amount:")
r = input("Enter rate of interest:")
t = input("Enter time period:")

p = float(p)
r = float(r)
t = float(t)
R = r/100

i = p*(1+R)**t

print("Compound interest is:",i)
