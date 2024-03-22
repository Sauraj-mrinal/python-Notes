# taking input from user 
#  here  we use a built-in function input \
    # what is input function in python ?
    
    # The input() function in Python is used to take input from the user.
    # It returns a string by default, which can be converted to other data types such as integers or floats using functions like int() or float(). 
    # The function can also take an optional parameter prompt, which is a string that 
    # is displayed to the user before they input their data.
    
    
    # take list as input from user
input_list = input("Enter a list: ").split()
print(f'The list is: {input_list}')


user_name = input("what is your name ")