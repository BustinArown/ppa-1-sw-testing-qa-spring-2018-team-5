
#this function finds the distance between two points (x1,y1) and (x2,y2)
import math

#def distance(x1,y1,x2,y2):
#    print 'x1=',x1, "\n" 'y1=',y1, "\n" 'x2=',x2, "\n" 'y2=',y2
#    if x2>x1 and y2>y1:
#        print 'x2-x1=',(x2 - x1)  ,"\n",'y2-y1=',(y2-y1)
#        print "(x2-x1)**2=",((x2-x1)**2),"\n",'(y2-y1)**2=', ((y2-y1)**2)
##        print 'square root of ((x2-x1)**2) + ((y2-y1)**2)=', round((math.sqrt(((x2-x1)**2) + ((y2-y1)**2))),4)
#    else:
#        print "x2 and y2 must be greater than x1 and y1"


def subtract (x1,y1,x2,y2):
    if x2>x1 and y2>y1:
        #return "SUBTRACT (x2-x1), (y2-y1)"
        return (x2-x1), (y2-y1)
    else:
        raise ValueError('x2 and y2 must be greater than x1 and y1 respectively')


def square (x1,y1,x2,y2):

        # "SQUARE ((y2-y1)**2), ((y2-y1)**2)"
        return (x2-x1)**2, (y2-y1)**2


def add(x1,y1,x2,y2):

        #print "ADD (((x2-x1)**2) + ((y2-y1)**2))"
        return ((x2-x1)**2) + ((y2-y1)**2)

def distance (x1,y1,x2,y2):

        #print "DISTANCE= (squareroot of(((x2-x1)**2) + ((y2-y1)**2)))"
        return float(round((math.sqrt(((x2-x1)**2) + ((y2-y1)**2))),4))

def enterValues():

    x1=int(input("x1="))
    y1=int(input("y1="))
    x2=int(input("x2="))
    y2=int(input("y2="))


    if x2>x1 and y2>y1:
        print subtract(x1,y1,x2,y2)
        print square(x1,y1,x2,y2)
        print add(x1,y1,x2,y2)
        print distance(x1,y1,x2,y2)
    else:
        raise ValueError('x2 and y2 must be greater than x1 and y1 respectively')


def main():
    enterValues()
if __name__ == '__main__':main()
