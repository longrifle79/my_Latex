#Gary Hobson
# Southern New Hampshire University
# IT140 Module 2

# ask for name and age
user_name = input('What is your name? ')  
user_age = int(input('How old are you? '))  
current_year = 2025 # assuming the current year is 2025
# Calculate the year of birth
birth_year = current_year - user_age
# Print the result
print(f'Hello {user_name}! You were boorn in {birth_year}.')
