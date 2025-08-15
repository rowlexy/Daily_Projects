from pprint import pprint

"""
The program should:
Prompt the user to enter a name, phone, and email.
Save the information to a .csv file (e.g. contacts.csv).
Add a feature to display all saved contacts (formatted nicely in the terminal).

"""

# When you run the program, it should:
# Ask the user to input name, phone, and email.
# Save that data to a CSV file.
# Ask if the user wants to view all saved contacts.
# If yes, it should print all contacts from the CSV.

def getContact():
    f_name = input('Enter your first name: ')
    l_name = input('Enter your last name: ')
    email = input('Enter your email address: ')
    phone = input('Enter your phone number: ')
    with open('contact.csv', 'a') as contact:
        info = f'{f_name} {l_name},{email},{phone}\n'
        contact.write(info)
        
    details = input('Do you want to view the details? (y/n): ')
    if details.lower() == 'y':
        with open('contact.csv', 'r') as contact:
            for detail in contact:
                pprint(detail.strip())

getContact()