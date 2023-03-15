#Tip Calculator!!

bill = float(input('Welcome to the tip calculator! \nWhat was the total bill? $'))
people = int(input('How many people to split the bill? '))
porcent = int(input('What percentage tip do you want to give?\n10, 12 or 15\n'))

mount = round((bill + bill * porcent*0.01)/people, 2) 
mount = "{:.2f}".format(mount) 

print(f'Each person should pay: ${mount}')