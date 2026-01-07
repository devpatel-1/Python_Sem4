# Develop a program that takes length measurements in centimeters and displays equivalent values in meters, kilometers, inches, and feet using appropriate mathematical operations (1 inch = 2.54 cm, 1 foot = 30.48 cm).

cm = float(input("Enter length in centimeters: "))

meter = cm / 100
km = cm / 100000
inch = cm / 2.54
feet = cm / 30.48

print("\n------ LENGTH CONVERSION ------")
print("Centimeters :", cm, "cm")
print("Meters      : {:.2f} m".format(meter))
print("Kilometers  : {:.5f} km".format(km))
print("Inches      : {:.2f} in".format(inch))
print("Feet        : {:.2f} ft".format(feet))
print("-------------------------------")