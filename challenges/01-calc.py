# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

operation = input(
    'What calculation would you like to do? (+, -, *, /) ')
num1 = int(input('what would you like the first number to be?'))
num2 = int(input('what would you like the second number to be?'))

# if operation == '+':
#   print(int(num1) + int(num2))
# elif operation == '-':
#   print(int(num1) - int(num2))
# elif operation == '*':
#   print(int(num1) * int(num2))
# elif operation == '/':
#   print(num1 / num2)
# else:
#   print('please make a valid selection')

# OR a dictionary


math = {
    '+': num1 + num2,
    '-': num1 - num2,
    '*': num1 * num2,
    '/': num1 / num2
}
print(math[operation])
