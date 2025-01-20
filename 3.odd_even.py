'''Write two functions, isOdd() and isEven(), with a single numeric parameter named
number. The isOdd() function returns True if number is odd and False if number is even. The
isEven() function returns the True if number is even and False if number is odd. '''

def isOdd(number):
        return  number%2!=0 
    
    
def isEven(number):
    return number%2==0 

num=int(input("Enter a number: "))
print("Odd:",isOdd(num))
print("Even:",isEven(num))
 