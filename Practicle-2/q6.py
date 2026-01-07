# Write a python program for the library charges to fine for books returned late. Following are the fines: 
# First five days: 40 paisa per day.
# Six to ten day: 65 paisa per day. 
# Above ten days: 80 paisa per day

days = int(input("Enter the number of days late: "))

fine = 0

if days <= 5:
    fine = days * 0.40
elif days <= 10:
    fine = (5 * 0.40) + (days - 5) * 0.65
else:
    fine = (5 * 0.40) + (5 * 0.65) + (days - 10) * 0.80

print("Total fine = Rs.", fine)