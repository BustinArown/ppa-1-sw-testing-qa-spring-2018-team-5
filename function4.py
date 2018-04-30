#!/usr/bin/python3

import cgi
import cgitb
cgitb.enable()
import math
import re


input_data=cgi.FieldStorage()



def email_verifier(address): 
    check = re.compile("[.][.]").search(address) is None and \
           re.compile("[a-z][a-z0-9!$%^*+-={|}._?~]*[@][a-z0-9!$%^*+-={|}_?~]+[.][a-z0-9!$%^*+-={|}_?~]+",
                      re.IGNORECASE).match(address) is not None
    if (check):
        print ("It is a valid address")
    else:
        print ("It is not a valid address")	

def main():  
    print ("Content-type: text/html")
    print ("")
    print ("<html><head>")
    print ("</head>")
    print ("<body>")
    try:    
        address = input_data["address"].value
        if (address == ""):
            raise ValueError
    except ValueError:
        print ("Wrong Input") 
        return    
    email_verifier(address)
      
    print ("</body></html>")
    	
    
if __name__ == '__main__':
    main()
 

