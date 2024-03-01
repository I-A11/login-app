# # Islam Aboamh date: 29/02/2024
# # This program to create new user account
# # Check existing user (for a previously registered user) and checks if they have a valid entry
# # Displays a numbered list of the existing user accounts
#
#
def check_password_length(password, min_length):
    # Create function to check password length
    return len(password) >= min_length


def add_user():
    # Prompt user to enter username
    username = input('Please enter username: ')

    # Validate username to ensure it's not empty
    while not username.strip():
        print('Username cannot be empty.')
        username = input('Please enter username again: ')
    # Prompt user to enter password
    password = input('Please enter password, it should be at least 10 characters long: ')

    min_length = 10

    # Validate password length
    while not check_password_length(password, min_length):
        print('Password should be at least 10 characters long.')
        password = input('Please enter password again: ')

    # Add username and password to accounts.txt file.
    with open('accounts.txt', 'a') as file:
        file.write(f'{username},{password}\n')

    print("User added")


def login():
    # Prompt user to enter username and password
    username = input('Please enter your username: ')
    password = input('Please enter your password: ')

    # Check username and password in accounts.txt file.
    with open('accounts.txt', 'r') as file:
        for line in file:
            stored_username, stored_password = line.strip().split(',')
            if username == stored_username and password == stored_password:
                print('Login successful')
                return True
    print('Invalid username or password')
    return False


def view_accounts():
    # Display numbered list for accounts.
    with open('accounts.txt', 'r') as file:
        for i, line in enumerate(file, 1):
            stored_username = line.strip().split(',')
            print(f"{i}. {stored_username[0]}")


def main():
    # Main function to control the flow of the program
    logged_in = False

    while True:
        print('Welcome to login program.')
        if logged_in:
            print('1. Add a new user.')
            print('2. Display users list.')
            print('3. Logout.')
            print('4. Exit the program.')
        else:
            print('1. Sign up for new users.')
            print('2. Login for existing users.')
            print('3. Exit the program.')

        try:
            # Prompt user for choice
            user_choice = input('Enter your choice please: ')
        except KeyboardInterrupt:
            print('\nExiting the program now.')
            user_choice = '3'

        if logged_in:
            if user_choice == '1':
                # Call function to add a new user
                add_user()
            elif user_choice == '2':
                # Call function to view accounts list
                view_accounts()
            elif user_choice == '3':
                # Logout
                logged_in = False
                print('Logged out successfully.')
            elif user_choice == '4':
                # Exit the program
                print('Exiting the program...')
                break
            else:
                # Handle invalid choice
                print('Invalid choice. Please try again.')
        else:
            if user_choice == '1':
                # Call function to add a new user
                add_user()
            elif user_choice == '2':
                # Call function to login
                if login():
                    logged_in = True
            elif user_choice == '3':
                # Exit the program
                print('Exiting the program...')
                break
            else:
                # Handle invalid choice
                print('Invalid choice. Please try again.')


if __name__ == "__main__":
    # Run the main function if the script is executed directly
    main()
