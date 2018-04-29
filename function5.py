#!/usr/bin/python3

import cgi
import cgitb
cgitb.enable()

import math

input_data=cgi.FieldStorage()

def splitTip(total, guestnumber):
    total+=total*0.15 #Calculate and add gratuity with the total amount
    total=round(total*100)/100  #Make total round upto 2 decimal points
    splittedtips = []   # This list contains the tips for all guests
    tip=math.floor(total*100/guestnumber)/100  #Compute the minimum amount given by each guest
    for x in range(0, guestnumber): #Distribute the minimum amount to each guest
        splittedtips.append(tip)
    remaining = round(total - tip*guestnumber, 2) #Compute the remaining tip that need to be equally distributed among the guests
    if (remaining>0.0):
        extra =  remaining/.01  #number of guests who will pay the remaining amount
        for k in range(round(extra)):
            splittedtips[k] += 0.01   #Distribute the remaining amount to the guests from the begining of the list
            splittedtips[k] = round(splittedtips[k], 2)
    
    print ("<h1>")
    print (splittedtips)	
    print ("</h1>")
    return splittedtips	
   
def processInput(input_amount, input_guest):
    try:
        input_amount = float(input_amount)
        if(input_amount<0):
            raise ValueError 
    except ValueError:
        print ("Wrong Amount")
        return
    try:
        input_guest = int(input_guest)
        if(input_guest<=0):
            raise ValueError    
    except ValueError:
        print ("Wrong Guest Number")
        return
    splitTip(input_amount, input_guest) #call the function with the input parameters
 
def main():
    print ("Content-type: text/html")
    print ("")
    print ("<html><head>")
    print ("</head>")
    print ("<body>")
    try:
        input_amount = float(input_data["num1"].value)
    except ValueError:
        print ("Wrong Amount")
        return
    try:	
    	   input_guest = int(input_data["num2"].value)
    except ValueError:
        print ("Wrong Guest Number")
        return

    #input_amount = input("Enter total amount")
    #input_guest = input("Enter total guests")
    processInput(input_amount, input_guest)
    print ("</body></html>")

    
if __name__ == '__main__':
    main()
 
