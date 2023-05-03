
primary_1 = input('Please enter a primary color.\n')
primary_2 = input('Please enter a primary color.\n')

if primary_1 == 'red' and primary_2 == 'blue':
    print('Your secondary color is purple!')
elif primary_1 == 'red' and primary_2 == 'yellow':
    print('Your secondary color is orange!')
elif primary_1 == 'blue' and primary_2 == 'yellow':
    print('Your secondary color is green!')
elif primary_1 == 'blue' and primary_2 == 'red':
    print('Your secondary color is purple!')
elif primary_1 == 'yellow' and primary_2 == 'red':
    print('Your secondary color is orange!')
elif primary_1 == 'yellow' and primary_2 == 'blue':
    print('Your secondary color is green!')
else:
    print('Incorrect primary color(s). Please try again.')
