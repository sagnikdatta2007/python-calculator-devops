import os 
import sys 

import math 



def calculate(a ,  operator ,b ):
    if operator == "+":
        return a+b 
    elif operator == "-":
        return a-b
     

    elif operator == "*":
        return a * b

    elif operator == "/":
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    else:
        raise ValueError("Invalid operator")

def main():
    print("--------------------------------------")
    print("         Python Devops Calculator            ")
    print("======================================")
    print("Available Operations + - * /")
    print("Press Q  to quit ")
    
    while True:
        operator = input("Enter an Operator")
        if operator.lower() == "q":
            print("exiting the calculator")
            break
        
        if operator not in [ "+" , "-" , "*" , "/"]:
            print("Invalid Operator")
            continue
        
        try:
            a = float(input("Enter the first number"))
            b = float(input("Enter the second number"))
            
            result = calculate( a,  operator ,b )
            print("===============================")
            print(result)
            
        except  ValueError as error:
            print("Error" , error)
            
            
            
            

            






if __name__ == "__main__":
    main()
    