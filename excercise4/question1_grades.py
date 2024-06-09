
# %% Question 1 grades
# Avraham Parshan 341419323
from Targil4input import *


# functional only
# document code - every line - base, general case for recursive
# recursion - write tail recursion or not

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
    get_students = lambda teach: list(
        filter(lambda stude: fn(stude, teach), list1))
    get_student_ids = lambda students: [student[0] for student in students]

    get_stats = lambda teach: (  # if avg or std is None, return empty tuple and not None
        (avg(teach), std(teach)) if avg(
            teach) is not None and std(teach) is not None else ()
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
    # now for each teacher, we have the students and their stats
    return L, calculateAvg(list1), calculateStandardDeviation(list1)


def myStudDict(Lst):
    """
     receives a list Lst of the same kind as the list which 
    is the first element of the tuple returned by the function myStudList. The function myStudDict will create 
    and return a dictionary D in which every key will be the name of a teacher, and the value bound to it will be 
    a list whose elements, except the last one, are the IDs of all the students of that teacher; the last element will 
    be a tuple of size 2 containing the grades average and the grades standard deviation of those students. 
    """
    # create dictionary
    dic = {teach[0]: (teach[1], teach[2]) for teach in Lst}
    # add last element which is a tuple with average and std of all students
    dic['All'] = (calculateAvg(jctMarks), calculateStandardDeviation(jctMarks)) #key is All and value is list with avg, and std
    return dic 


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
    if len(newL) == 0: #nothing to do
        return None
    return sum(newL) / len(newL) #mean 


def calculateVariance(marks: list):
    """
    given a list of marks, return the variance
    """
    avg = calculateAvg(marks)
    grades = getGradesFromList(marks)
    if len(grades) == 0: #nothing to do
        return None
    return sum((x - avg) ** 2 for x in grades) / len(grades) #sigma with the cur - mu etc..


def calculateStandardDeviation(marks: list):
    cv = calculateVariance(marks)
    if cv == None: # nothing to do 
        return None
    return calculateVariance(marks)**0.5  # square root of variance


def main():
    print("Printing results")
    res = myStudList(jctMarks, teacherName)
    print(res)

    print("Printing dictionary")
    print(myStudDict(res[0]))


if __name__ == "__main__":
    main()
