
# functional only
# document code - every line - base, general case for recursive
# recursion - write tail recursion or not
#
# %% Question 1 grades
# Avraham Parshan 341419323
from Targil4input import *
from tailrecurse import *


def myStudList(list1: list, list2: list):
    """
    given list1 = jctMarks, list2 = teacherName
    # list L, every element is list , 1st elem is name of teacher, 2nd list size 2 first elmen = list ids of students of teacher
    # 2nd tuple with avg and std of grades of all students
    # if no students in course with teacher return empty part of list
    """


    # filter to get the students of the teacher
    fn = lambda student, teacher: student[2] == teacher[1]
    # Helper functions for average and standard deviation
    get_students = lambda teach: list(filter(lambda stude: fn(stude, teach), list1))
    get_student_ids = lambda students: [student[0] for student in students]

    get_stats = lambda teach: ( #if avg or std is None, return empty tuple and not None
        (avg(teach), std(teach)) if avg(teach) is not None and std(teach) is not None else ()
    )

    avg = lambda teach: calculateAvg(get_students(teach))
    std = lambda teach: calculateStandardDeviation(get_students(teach))
    
    # process the teacher to display the information in desired format
    process_teacher = lambda teach: [
        teach[0], 
        get_student_ids(get_students(teach)), 
        get_stats(teach)
    ]
    L = list(map(process_teacher, list2))
    return L, calculateAvg(list1), calculateStandardDeviation(list1) #now for each teacher, we have the students and their stats

def myStudDict(Lst):
    """
    that receives a list Lst of the same kind as the list which 
is the first element of the tuple returned by the function myStudList. The function myStudDict will create 
and return a dictionary D in which every key will be the name of a teacher, and the value bound to it will be 
a list whose elements, except the last one, are the IDs of all the students of that teacher; the last element will 
be a tuple of size 2 containing the grades’ average and the grades’ standard deviation of those students. 
    """

    #TODO NOT WORKING RN 
    # Helper functions for average and standard deviation
    get_students = lambda teach: list(filter(lambda stude: stude[2] == teach[1], jctMarks))
    get_student_ids = lambda students: [student[0] for student in students]

    get_stats = lambda teach: ( #if avg or std is None, return empty tuple and not None
        (avg(teach), std(teach)) if avg(teach) is not None and std(teach) is not None else ()
    )

    avg = lambda teach: calculateAvg(get_students(teach))
    std = lambda teach: calculateStandardDeviation(get_students(teach))
    
    # process the teacher to display the information in desired format
    process_teacher = lambda teach: [
        # teach[0], 
        get_student_ids(get_students(teach)), 
        # get_stats(teach)
    ]

    # create dictionary
    return {teach[0]: process_teacher(teach) for teach in Lst}

def getSubjFromTeacher(teach: str, teachList: list = teacherName):
    """
    given a teacher name, return the subjects he teaches
    """
    fn = lambda x: x[0] == teach
    li = list(filter(fn, teachList))
    if len(li) == 0:
        return None
    return li[0][1]     # only return 1 string = subject


def calcAvgStd(subject: str, marks: list):
    """
    given a subject name and marks, return the average and standard deviation of the students
    """
    # filter the marks of the teacher
    fn = lambda x: x[2] == subject
    marks = list(filter(fn, marks))
    # calculate the average and standard deviation
    avg = calculateAvg(marks)
    std = calculateStandardDeviation(marks)
    if avg == None or std == None:
        return ()
    return (avg, std)


def getGradesFromList(marks: list):
    """
    student, grade, subject
    extract grades from list and return as list
    """
    return [x[1] for x in marks]


def calculateAvg(marks: list):
    """
    given a list of marks, return the average
    """
    newL = getGradesFromList(marks)
    if len(newL) == 0:
        return None
    return sum(newL) / len(newL)


def calculateVariance(marks: list):
    """
    given a list of marks, return the variance
    """
    avg = calculateAvg(marks)
    grades = getGradesFromList(marks)
    if len(grades) == 0:
        return None
    return sum((x - avg) ** 2 for x in grades) / len(grades)


def calculateStandardDeviation(marks: list):
    cv = calculateVariance(marks)
    if cv == None:
        return None
    return calculateVariance(marks)**0.5  # square root of variance


def main():
    print("Average: ")
    print(calculateAvg(jctMarks))
    print("Variance: ")
    print(calculateVariance(jctMarks))
    print("Standard Deviation: ")
    print(calculateStandardDeviation(jctMarks))

    print("Avg and Std of subject: ")
    sub = 'Computer'
    print(calcAvgStd(sub, jctMarks))

    print(getSubjFromTeacher('Zloti'))

    print("all together")
    res = myStudList(jctMarks, teacherName)
    print(res)
    
    print("Dictionary")
    print(myStudDict(res[0]))
    pass


if __name__ == "__main__":
    main()
