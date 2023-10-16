
"""

Lets start with the logic because understanding what you are trying to do is important.

If you don't understand both the problem you are trying to solve and the logic to solve it, 
you will obviously never be able to create an algorithm to solve the problem..

Problem:  
Work out if a given year is a leap year

Logic:
Any year divisible by 4 that is not a century year is a leap year
If the year is divisible by 4 AND a century year (i.e divisible evenly by 100) only 1 in 4 of these are century years so we need another check for these years
So for these centurn years, we check if they are divisible evenly by 400, if it is then it is a leap year

"""

# While True just makes this code loop forever.  It will just keep asking you over and over to enter years
while True:

    # Set the LeapYear to False to begin with 
    LeapYear = False

    # Ask the user to enter a year
    # Note I am converting the entered data to an integer because a year is an integer and python input function returns text by default
    # I'm using use try / except to catch problems. If the user enters a letter and I try to convert it to an integer, the program will crash 
    # and try/except will catch this and save the program (try it)
    try:
        year = int(input("Enter year : "))
    except:
        print ('Not a valid year')
        exit()


    # Now my logic
    # If the year is divisible evenly by 4 it is a leap year
    # However if the year is a century then we have to check it it is divisible by 400 as century years are special
    # Only 1 in 4 century years are leap years

    if (year % 4) == 0:                     # Check evenly divisible by 4
        if (year % 100) == 0:               # Now check if it is a century year
            if (year % 400) == 0:           # If it is a centurn check it is divisible by 400 evenly 
                print ('Its a leap Year')
            else:
                print ('Its not a leap Year')
        else:
            print ('Its a leap Year')
    else:     
        print ('Its not a leap Year')
 
    print ()



    