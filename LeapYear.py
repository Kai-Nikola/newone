"""print("Program to check leap year")

year = int(input("Year: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('Leap Year')
else:
    print('Normal year')"""
    
'''second method'''    

year = int(input("Year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print('Not a Leap year')
    else:
        print("Leap Year")   
else:
    print("Not a leap year")
        
        
