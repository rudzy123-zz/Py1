#Rudolf Musika
#CIS 1400
#Chapter 8 Assignment

# This Program has two parallel arrays

def main():

# Enter the user name  you need
 nameEntered = input("Enter the first and last name of a friend to search for: ")

 global index
 index = 0
 list = getName()
 phoneNumber = getNumber()
 found = False

 # Create a loop to act as a loop counter
 while found == False and index < len(phoneNumber):
    if nameEntered == list[ index]:
          found = True
    else:
        index = index + 1
          
 if found:
              print("found ",nameEntered,"Phone Number: ",phoneNumber[index])
 else:
               print(nameEntered,"NOT Found!")
              
def getName():
    name = [ "Mike Bolton"," Rich Smith", "Amy Nelson","Jan Jones","Pat Allen","Mary Davis" ]
    return name

def getNumber():
    number = ["630-882-7080"," 630-453-0911"," 630-922-1844","630-672-007","630-880-1122","630-554-5883"]
    return number

    
main()
