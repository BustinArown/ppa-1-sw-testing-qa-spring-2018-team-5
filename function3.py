#!/usr/bin/python3

import cgi
import cgitb
cgitb.enable()
import math

input_data=cgi.FieldStorage()

def shortest_distance(x1, y1, x2, y2):  # this function finds the distance between two points (x1,y1) and (x2,y2)
    return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 4)

def main():  
    print ("Content-type: text/html")
    print ("")
    print ("<html><head>")
    print ("</head>")
    print ("<body>")
    try:
        x1 = float(input_data["x1"].value)
    except ValueError:
        print ("Wrong X1")
        return
    try:
        y1 = float(input_data["y1"].value)
    except ValueError:
        print ("Wrong Y1")
        return
    try:
        x2 = float(input_data["x2"].value)
    except ValueError:
        print ("Wrong X2")
        return
    try:
        y2 = float(input_data["y2"].value)
    except ValueError:
        print ("Wrong Y2")
        return

    distance = shortest_distance(x1, y1, x2, y2)
    print ("<h3>")
    print ("Shortest Distance is :", distance)
    print ("</h3>")
        
    print ("</body></html>")
    	
    
if __name__ == '__main__':
    main()
 
