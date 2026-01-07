# Create a program that takes Principal amount (P), Rate of interest (R), and Time period (T) in months from user and calculates:
# Simple Interest: (P × R × T)/100
# Total Amount: P + SI
# Display all values properly formatted.


p = float(input("Enter Principal Amount (Rs): "))
r = float(input("Enter Rate of Interest (%): "))
t = float(input("Enter Time Period (months): "))

# Convert months into years
t_years = t / 12

si = (p * r * t_years) / 100
total = p + si

print("\n------ INTEREST DETAILS ------")
print("Principal Amount : Rs.{:.2f}".format(p))
print("Rate of Interest : {:.2f}%".format(r))
print("Time Period      : {} months".format(t))
print("Simple Interest  : Rs.{:.2f}".format(si))
print("Total Amount     : Rs.{:.2f}".format(total))
print("------------------------------")