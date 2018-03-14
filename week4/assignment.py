# Histogram
'''
Write a Python function histogram(l) that takes as input a list of integers with repetitions and returns a list of pairs as follows:

    for each number n that appears in l, there should be exactly one pair (n,r) in the list returned by the function, where r is is the number of repetitions of n in l.

    the final list should be sorted in ascending order by r, the number of repetitions. For numbers that occur with the same number of repetitions, arrange the pairs in ascending order of the value of the number.

For instance:

>>> histogram([13,12,11,13,14,13,7,7,13,14,12])
[(11, 1), (7, 2), (12, 2), (14, 2), (13, 4)]

>>> histogram([7,12,11,13,7,11,13,14,12])
[(14, 1), (7, 2), (11, 2), (12, 2), (13, 2)]

>>> histogram([13,7,12,7,11,13,14,13,7,11,13,14,12,14,14,7])
[(11, 2), (12, 2), (7, 4), (13, 4), (14, 4)]
'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def histogram(data):
    data.sort()
    if len(data) < 1:
        return []
    final_list = []
    frequency_dict = {}
    current = data[0]
    count = 0
    for element in data:
        if element != current:
            if count not in frequency_dict:
                frequency_dict[count] = []
            frequency_dict[count].append(current)
            count = 0
            current = element
            count += 1
        else:
            count += 1
    if count not in frequency_dict:
        frequency_dict[count] = []
    frequency_dict[count].append(current)
    temp = list(frequency_dict.keys())
    temp.sort()
    for i in temp:
        frequency_dict[i].sort()
        for j in frequency_dict[i]:
            final_list.append((j, i))
    return final_list


# TRANSCRIPT
'''
A college maintains academic information about students in three separate lists.

    Course details: A list of pairs of form (coursecode,coursename), where both entries are strings.
    For instance, [("MA101","Calculus"),("PH101","Mechanics"),("HU101","English")]

    Student details: A list of pairs of form (rollnumber,name), where both entries are strings.
    For instance, [("UGM2018001","Rohit Grewal"),("UGP2018132","Neha Talwar")]

    Grades: A list of triples of the form (rollnumber,coursecode,grade), where all entries are strings.
    For instance, [("UGM2018001", "MA101", "AB"), ("UGP2018132", "PH101", "B"), ("UGM2018001", "PH101", "B")].
    You may assume that each roll number and course code in the grade list appears in the student details and course details, respectively.

Your task is to write a function transcript(coursedetails,studentdetails,grades) that takes these three lists as input and
produces consolidated grades for each student. Each of the input lists may have its entries listed in arbitrary order.
Each entry in the returned list should be a tuple of the form

(rollnumber, name,[(coursecode_1,coursename_1,grade_1),...,(coursecode_k,coursename_k,grade_k)])

where the student has grades for k >= 1 courses reported in the input list grades.

The output list should be organized as follows.

    The tuples shold sorted in ascending order by rollnumber

    Each student's grades should sorted in ascending order by coursecode

For instance:

>>> transcript([("MA101","Calculus"),("PH101","Mechanics"),("HU101","English")],[("UGM2018001","Rohit Grewal"),("UGP2018132","Neha Talwar")],[("UGM2018001","MA101","AB"),("UGP2018132","PH101","B"),("UGM2018001","PH101","B")])
[('UGM2018001', 'Rohit Grewal', [('MA101', 'Calculus', 'AB'), ('PH101', 'Mechanics', 'B')]), ('UGP2018132', 'Neha Talwar', [('PH101', 'Mechanics', 'B')])]

>>> transcript([("T1","Test 1"),("T2","Test 2"),("T3","Test 3")],[("Opener","Murali Vijay"),("Captain","Virat Kohli"),("No3","Cheteshwar Pujara")],[("Opener","T1","14"),("Captain","T1","33"),("No3","T1","30"),("Opener","T2","55") ,("Captain","T2","158"),("No3","T2","19"), ("Opener","T3","33"),("Captain","T3","95"),("No3","T3","51")])
[('Captain', 'Virat Kohli', [('T1', 'Test 1', '33'), ('T2', 'Test 2', '158'), ('T3', 'Test 3', '95')]), ('No3', 'Cheteshwar Pujara', [('T1', 'Test 1', '30'), ('T2', 'Test 2', '19'), ('T3', 'Test 3', '51')]), ('Opener', 'Murali Vijay', [('T1', 'Test 1', '14'), ('T2', 'Test 2', '55'), ('T3', 'Test 3', '33')])]

'''


def transcript(coursedetails, studentdetails, grades):
    course_dict = {}
    student_dict = {}
    for i in coursedetails:
        course_dict[i[0]] = i[1]
    for i in studentdetails:
        student_dict[i[0]] = i[1]
    roll_no = []
    for roll_nos in student_dict.keys():
        roll_no.append(roll_nos)
    roll_no.sort()
    grades.sort()
    final_list = []
    for i in roll_no:
        individual_tuple = ()
        individual_tuple += (i, student_dict[i])
        grade_list = []
        for j in grades:
            if j[0] == i:
                grade_list.append((j[1], course_dict[j[1]], j[2]))
        individual_tuple += (grade_list,)
        final_list.append(individual_tuple)
    return final_list

