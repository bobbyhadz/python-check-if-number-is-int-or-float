# Check if a number is an int or float in Python

my_num = 1357

if isinstance(my_num, int):
    print('number is int')

if isinstance(my_num, float):
    print('number is float')

# -----------------------------------

# ✅ checks if a number is either int or float

if isinstance(my_num, (int, float)):
    print('Number is either int or float')