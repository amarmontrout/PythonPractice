
p1 = input('Please enter a primary color (Red, Blue or Yellow): ')
p2 = input('Please enter a primary color (Red, Blue or Yellow): ')

if (p1.lower() == 'red' and p2.lower() == 'blue') or (p1.lower() == 'blue' and p2.lower() == 'red'):
    print('Your secondary color is purple!')
elif (p1.lower() == 'red' and p2.lower() == 'yellow') or (p1.lower() == 'yellow' and p2.lower() == 'red'):
    print('Your secondary color is orange!')
elif (p1.lower() == 'blue' and p2.lower() == 'yellow') or (p1.lower() == 'yellow' and p2.lower() == 'blue'):
    print('Your secondary color is green!')
elif p1 == p2:
    print(p1.lower())
else:
    print('Incorrect color(s). Please try again.')
