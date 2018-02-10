import math

def splitTip(total, guestnumber):
    total+=total*0.15 #Calculate and add gratuity with the total amount
    total=round(total*100)/100  #Make total round upto 2 decimal points
    print(total)
    splittedtips = []   # This list contains the tips for all guests
    tip=math.floor(total*100/guestnumber)/100  #Compute the minimum amount given by each guest
    print(tip)
    for x in range(0, guestnumber): #Distribute the minimum amount to each guest
        splittedtips.append(tip)
        
    remaining = total - tip*guestnumber #Compute the remaining tip that need to be equally distributed among the guests
    print(remaining)
    if (remaining>0.0):
        extra =  remaining/.01  #number of guests who will pay the remaining amount
        for k in range(round(extra)):
            splittedtips[k] += 0.01   #Distribute the remaining amount to the guests from the begining of the list
    print(splittedtips)
    return splittedtips

def takeInput():
    input_amount = input("What is the total amount?") #take input for bill amount
    input_guest =  input("How many guests?") #take input for number of guests
    try:
        input_guest = int(input_guest)
    except ValueError:
        print("This is a wrong number, please try again.")
        return
    try:
        input_amount = float(input_amount)
    except ValueError:
        print("This is a wrong amount, please try again.")
        return
          
    splitTip(input_amount, input_guest) #call the function with the input parameters

def main():
    takeInput()
    
    
    
if __name__ == '__main__':
    main()
 