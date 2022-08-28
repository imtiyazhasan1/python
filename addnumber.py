
###create file with addnumber.py and run the command python3 addnumber.py. Put below content into the file
# Store input numbers
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

# Add two numbers
sum = float(num1) + float(num2)

# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
### another way
print('The sum of ' + num1 + ' and {1} is {2}'.format(num1, num2, sum))
