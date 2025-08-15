# The program should:
# Let the user attempt to enter a password.
# Give them up to 3 tries using a while loop.
# If the user enters the correct password within 3 tries, print a success message like "Access granted."
# If the user fails 3 times, print "Too many attempts. You are locked out."
# You can hardcode the correct password as "python123" for this exercise.


def checkPassword():
    try:
        correct_password = "python123"
        attempts = 3
        while attempts > 0:
            user_password = input('Enter your password: ')
            if user_password == correct_password:
                print("Access granted")
                break
            else:
                attempts -= 1
                if attempts > 0:
                    print(f'Incorrect password {attempts} attempt(s) remaining..')
                else:
                    print("Too many attempts. You are locked out.")          
    except KeyboardInterrupt:
        print('Exited the loop')
                    
checkPassword()