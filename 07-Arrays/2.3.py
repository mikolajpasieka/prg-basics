# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
total = 0 
count_food = 0 
count_transport = 0 
count_utilities = 0
count_1 = 0
count_2 = 0 
count_3 = 0 
count_4 = 0

for row in monthly_expenses:
    for i in row: 
        total += i 

for row in monthly_expenses:
    count_food += row[0]

for row in monthly_expenses:
    count_transport += row[1]

for row in monthly_expenses:
    count_utilities += row[2]

for i in monthly_expenses[0]:
    count_1 += i

for i in monthly_expenses[1]:
    count_2 += i

for i in monthly_expenses[2]:
    count_3 += i

for i in monthly_expenses[3]:
    count_4 += i

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',count_food)
print('Transport:',count_transport)
print('Utilities:',count_utilities)
print('Week 1:', count_1)
print('Week 2:',count_2)
print('Week 3:',count_3)
print('Week 4:',count_4)
print('---------------')
print('TOTAL:',total)