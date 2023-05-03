primary_colors = ['red', 'blue', 'yellow']
done = ['done']

while True:
    p1 = input('Please enter a primary color (Red, Blue or Yellow) or type "done" to exit: ')
    p2 = input('Please enter a primary color (Red, Blue or Yellow) or type "done" to exit: ')
    if (p1.lower() and p2.lower() in primary_colors) or (p1.lower() and p2.lower() in done):
        if (p1.lower() == 'red' and p2.lower() == 'blue') or (p1.lower() == 'blue' and p2.lower() == 'red'):
            print('Your secondary color is purple!')
        elif (p1.lower() == 'red' and p2.lower() == 'yellow') or (p1.lower() == 'yellow' and p2.lower() == 'red'):
            print('Your secondary color is orange!')
        elif (p1.lower() == 'blue' and p2.lower() == 'yellow') or (p1.lower() == 'yellow' and p2.lower() == 'blue'):
            print('Your secondary color is green!')
        elif (p1.lower() in done) or (p2.lower() in done):
            break
        else:
            print(p1.lower())
    else:
        print('Incorrect color(s). Try again or type "done" to exit.')
input('Goodbye.')
