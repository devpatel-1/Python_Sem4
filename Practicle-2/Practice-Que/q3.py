# Create a program that takes radius and height of a cylinder from user and calculates its volume (π × r² × h) and surface area (2π × r² + 2π × r × h). Display the results with proper units.

pi = 3.14159

r = float(input("Enter radius of cylinder (cm): "))
h = float(input("Enter height of cylinder (cm): "))

volume = pi * r * r * h
surface_area = 2 * pi * r * r + 2 * pi * r * h


print("\n----- CYLINDER DETAILS -----")
print("Radius       : {} cm".format(r))
print("Height       : {} cm".format(h))
print("Volume       : {:.2f} cubic cm".format(volume))
print("Surface Area : {:.2f} square cm".format(surface_area))
print("----------------------------")