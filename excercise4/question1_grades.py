
# functional only 
# document code - every line - base, general case for recursive
# recursion - write tail recursion or not 
#
# %% Question 1 grades
# Avraham Parshan 341419323
from Targil4input import *
from tailrecurse import *

def myStudList(list1, list2):
    """
    given list1 = jctMarks, list2 = teacherName
    """
    # list L, every element is list , 1st elem is name of teacher, 2nd list size 2 first elmen = list ids of students of teacher
    # 2nd tuple with avg and std of grades of all students
    # if no students in course with teacher return empty part of list
    teachers = list(map(lambda x: x[0], list2))
    #TODO finish
    
def getGradesFromList(marks: list):
    """
    student, grade, subject
    extract grades from list and return as list
    """
    return list(map(lambda x: x[1], marks))

def calculateAvg(marks: list):
    """
    given a list of marks, return the average
    """
    newL = getGradesFromList(marks)
    return sum(newL) / len(newL)

def calculateVariance(marks: list):
    """
    given a list of marks, return the variance
    """
    avg = calculateAvg(marks)
    newL = getGradesFromList(marks)
    return sum(list(map(lambda x: (x - avg)**2, newL)))/len(newL)

def calculateStandardDeviation(marks: list):
    return calculateVariance(marks)**0.5 # square root of variance

def main():
    print("Average: ")
    print(calculateAvg(jctMarks))
    print("Variance: ")
    print(calculateVariance(jctMarks))
    print("Standard Deviation: ")
    print(calculateStandardDeviation(jctMarks))
    
    print("all together")
    print(myStudList(jctMarks, teacherName))
    pass


if __name__ == "__main__":
    main()
