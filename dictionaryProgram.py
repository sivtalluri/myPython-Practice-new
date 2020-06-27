# git testing
# Student Ranks Program: this program total marks of each student and find the ranks among themselves.

import json

class classStudentMarks:
    def __init__(self, s, m):
        self.students = s
        self.marks = m
        self.studentTotalMarks = []
        self.record = []

    def studentNames(self):
        # studentName = self.student
        return self.students

    def studentRecords(self):
        for i in range(len(self.marks)):
            s = 0
            tempDict = {}
            for element in self.marks[i]:
                s += element
            self.studentTotalMarks.append(s)
            tempDict["name"] = self.students[i]
            tempDict["marks"] = self.marks[i]
            tempDict["totalMarks"] = self.studentTotalMarks[i]
            self.record.append(tempDict)
            # self.record[i] = tempDict
        return self.record


allStudentRecords = classStudentMarks(['Aravind', 'Prasad', 'Rohin'],
                                  ([98, 99, 100, 94, 96], [88, 89, 90, 84, 86], [98, 89, 90, 94, 96]))

studentJsonObj = allStudentRecords.studentRecords()
formattedJsonObj = json.dumps(studentJsonObj, indent=4)
print ("Class Student Marks Records : ", formattedJsonObj)
print("git testing")

#
# print("Student :", classAllStudentMarks.studentNames(),
#       "  Class All Subjects Total Marks : ", classAllStudentMarks.totalMarks())




