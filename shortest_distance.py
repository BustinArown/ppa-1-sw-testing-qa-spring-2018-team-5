
#this function finds the distance between two points (x1,y1) and (x2,y2)
import math

def distance (x1,y1,x2,y2):
    #return 0
    if x2 >= x1 and y2 >= y1:
        return (math.sqrt(((x2-x1)**2) + ((y2-y1)**2)))
    else:
        raise ValueError('x2 and y2 must be greater than x1 and y1 respectively')
    #round(math.sqrt(((x2-x1)**2) + ((y2-y1)**2)),2)


def floatValues(x1,y1,x2,y2):
    return float(x1),float(y1),float(x2),float(y2)
    #return float(math.sqrt(((x2-x1)**2) + ((y2-y1)**2)))



print distance(2,4,5,8)
#print not_zero (1,2,5,0)
#print floatValues(0,0,0,0)
