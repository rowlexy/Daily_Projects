# Ask the user to enter a number (e.g., 7).
# Use a for loop to print that number’s multiplication table from 1 to 12.
# Display each line in a readable format like 7 x 3 = 21.

def multiplicationTable():
    number = int(input('Enter a number: '))
    for i in range(1, 13, 1):
        display = f'{number} x {i} = {number * i}'
        print(display)
        
multiplicationTable()