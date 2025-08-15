"""
Ask the user to enter a starting number (e.g., 10).
Count down to 1 using a for or while loop, printing each number with a 1-second delay between prints.
After the countdown, display a final message like "Time’s up!" or "Go!".

💡 Bonus:
Add a check to ensure the user enters a positive integer.
Let the user choose the final message before the countdown begins.
"""
import time
def countDown():
    while True:
        try:
            number = int(input('Enter a starting number: '))
            if number <= 0:
                print('Enter a whole number greater than 0')
                continue
            display_message = input('Enter your final message: ')
            if not display_message:
                display_message = "Times's up!"
            
            for i in range(number, -1, -1):
                print(i)
                time.sleep(1)
            print(display_message)
            break
        except ValueError:
            print('Please enter a valid integer')
        except KeyboardInterrupt:
            print('\nExited the loop')
            break
        
               
countDown()