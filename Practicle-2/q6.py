# Write a python program for the library charges to fine for books returned late. Following are the fines: 
# First five days: 40 paisa per day.
# Six to ten day: 65 paisa per day. 
# Above ten days: 80 paisa per day

days = int(input("Enter number of late days: "))

if days <= 5:
    fine = days * 0.40
elif days <= 10:
    fine = days * 0.65
else:
    fine = days * 0.80

print("Total Fine = Rs. ", fine)

