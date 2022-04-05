print("Welcome to Chase bank.")

balance = 4000

operation = input(
    'If you would like to see your balance, press 1. If you would like a withdrawal, press 2. If you would like a deposit, press 3')
if (operation == '1'):
    print(balance)
elif (operation == '2'):
    withdrawal = int(input('How much would you like to withdraw?'))
    new_balance = str(balance - int(withdrawal))
    print('Your new balance is ' + new_balance)
elif (operation == '3'):
    deposit = input('How much would you like to deposit?')
    new_balance = balance + int(deposit)
    print('Your new balance is:')
    print(new_balance)
else:
    print('Please make a valid selection.')

done = input('Are you done? Y/N')
if (done == 'y' or 'Y'):
    print('Have a nice day')
elif (done == 'n' or 'N'):
    print('Yes you are. Get lost.')
else:
    print('Make a valid selection.')
