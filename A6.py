#RUDOLF T MUSIKA
#CIS1400
#CHAPTER 6 ASSIGNMENT

def main():
    #The number of grades to be entered in the program is 5 
    numberOfGrades()
    
    #The user is to enter the grades in a sequencial repititive manner
    #Once the 5 grades have been entered, the average of the grades will be calculated
    
    calcAverageOfGrades(numberOfGrades)

def numberOfGrades():
    global numberOfGrades
    numberOfGrades= 5
    
def calcAverageOfGrades(numberOfGradeN):
    calcAve = 0.0
    countGrade = 0

    for countY in range (numberOfGradeN):
         
        testscoreEnter = float(input("Enter test score:  "))

        checkGrade(testscoreEnter)
        
        
        calcAve = calcAve + testscoreEnter
        countGrade+= 1

    average = (calcAve)/(numberOfGrades)
         
    print("The average is: ",format(average,".1f"))

def checkGrade(gradeEntered):
    if (gradeEntered >=90 and gradeEntered <=100):
        result = print( " The letter grade is : A ")
        return result
    elif(gradeEntered >=80 and gradeEntered <=89):
        result = print( " The letter grade is : B ")
        return result
    elif(gradeEntered >=70 and gradeEntered <=79):
        result = print(" The letter grade is : C")
        return result
    elif(gradeEntered >=60 and gradeEntered <=69):
        result = print(" The letter grade is : D ")
        return result
    else:
        result = print(" The letter grade is : F ")
        return result

main()
