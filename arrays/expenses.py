
expenses = [ 2200, 2350, 2600, 2130, 2190 ]

# In feb, how many dollars you spent extra compared to january?
print("The total extra spent in feb compared to jan is " + str(expenses[1]-expenses[0]))


# Find out total expense in first quarter (first three months) of the year
print("The total expenses for the first quarter is " + str(expenses[0]+expenses[1]+expenses[2]))

# Find out if you spent exactly 2000 dollars in any month
print(2000 in expenses)

# June month just finished and your expense is 1980 dollars
# Add this item to our monthly expense list
expenses.append(1980)

# You returned an item that you bought in the month of april and got a refund of $200
# Make a correction to your monthly expense list
expenses[3] = expenses[3] - 200
print("Expenses after 200$ return in April:",expenses) 