#First, let's declare the variable meal and assign it the value 44.50. 
meal = 44.50
 
#Create the variable tax and set it equal to the decimal value of 6.75%.
meal = 44.50
tax = 0.0675

# Set the variable tip to decimal value of 15% on line 5.
meal = 44.50
tax = 0.0675
tip = 0.15

#On line 7, reassign meal to the value of itself + itself * tax. And yes, you're allowed to reassign a variable in terms of itself!
#We're only calculating the cost of meal and tax here. We'll get to the tip soon.
meal = 44.50
tax = 0.0675
tip = 0.15
meal = 47.50375

#Assign the variable total to the sum of meal + meal * tip on line 8. 
#Now you have the total cost of your meal!

meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + meal * tax
total = meal + meal * tip

print("%.2f" % total)