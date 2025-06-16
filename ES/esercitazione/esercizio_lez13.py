'''
def countdown(n):

    while n >= 0 :

        print(n)
        n -= 1

    if n < 0:

        print("Error: Please enter a positive integer.")

    
    
countdown(-5) 

print("---")

countdown(5)'''

'''
def countdown(n:int):

    if n >= 0 :
    
        while n:

            print(n)
            n -= 1
    
    else:

        print("Error! Inserted number is negative!")
    
countdown(-5)
countdown(5)'''