print("Hello, welcome to the ChatBot.")
name = input('What is your name? ')
age = input('What about your age? ')
help = input('How may I help you? ')

print('Choose from this list: \n')
print('1. \n') #Put something here
print('2. \n') #Put something here
print('3. \n') #Put something here
choiceTwo = 'y'
while choiceTwo == 'y':
    choice = input('\nType number answer here: ')
    if choice == '1':
        print('')#Place things here
    elif choice == '2':
        print('')#Place things here
    elif choice == '3':
        print('')#Place things here
    else:
        choice = input("Enter your choice again: ")
    choiceTwo = input('Would you like to go again(y/n)? ')
print(' ')