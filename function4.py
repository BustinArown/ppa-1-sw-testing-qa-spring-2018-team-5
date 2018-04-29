#!/usr/bin/python3

import cgi
import cgitb
cgitb.enable()
import math
import re


input_data=cgi.FieldStorage()



def email_verifier(address):
    return re.compile("[.][.]").search(address) is None and \
           re.compile("[a-z][a-z0-9!$%^*+-={|}._?~]*[@][a-z0-9!$%^*+-={|}_?~]+[.][a-z0-9!$%^*+-={|}_?~]+",
                      re.IGNORECASE).match(address) is not None

def main():  
    print ("Content-type: text/html")
    print ("")
    print ("<html><head>")
    print ("</head>")
    print ("<body>")
    
    address = input_data["address"].value
    if (email_verifier(address)):
        print (address, "is a valid email.")
    else:
        print (address, "is an invalid email.")
   
    print ("</body></html>")
    	
    
if __name__ == '__main__':
    main()
 

