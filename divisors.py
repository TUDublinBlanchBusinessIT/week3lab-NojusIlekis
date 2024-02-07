#Nojus Ilekis
#07/02/2024
#divisors.py

#Add a function below called divisors(num) which takes one argument of type integer
#and returns a list of all the divisors(factors) of that that number -
#A divisor or factor is a number which divides evenly leaving no remainder
def divisors(num):
    
#define the funciton header called divisors expecting one argument
    #set up an empty list to hold your result
    myList = []
    #loop i from 1 to the number you are checking (take care not to include the number itself)
    for i in range(1, num):
        if num % i == 0:
            myList.append(i)
        #if the remainder when dividing the number by i is equal to zero then i is a divisor so...
    return myList    
            #apend i to the list you set up
            
print(divisors(28))
    #return the list
    
