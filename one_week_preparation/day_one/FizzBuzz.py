
from sqlite3 import ProgrammingError
from xml.dom.minidom import Element


# fizzbuzz function
def FizzBuzz(n):
    for i in range(n):
        element = i+1
        print(element)
        # if (element %3) ==0 and (element%5) == 0:
        #     print("FizzBuzz")

        # elif (element%3) ==0:
        #     print("Fizz")

        # elif(element%5)==0:
        #     print("Buzz")

        # else:
        #     print(element)

numbers = 20
FizzBuzz(numbers)