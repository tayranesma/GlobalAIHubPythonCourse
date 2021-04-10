# -*- coding: utf-8 -*-

"""
Course Grade Application
* create 5 students. Ask these students from the user.
* each of these students should have a midterm grade, project grade, and final grade.
* each student will have a course passing grade
* passingGrade = midterm*(0.3) + project*(0.3) + final*(0.4) passing grade should be determined like this
* create a dictionary that keeps these students' information
* calculate the students' grades and transfer them to the list with help of indexing
* finally set the student with the highest grade to be in the first index and the student with the lowest grade to be in the last index of the list
"""
#Making students dictionary
students = {}
for i in range(5):
    name = input("Please insert an username: ")
    midterm = float(input("Please insert midterm grade: "))
    project = float(input("Please project grade: "))
    final = float(input("Please final grade: "))
    score = midterm*0.3 + project*0.3 + final*0.4
    students[name] = score
    
print("\n")  

#sort dictionary by descending order
sorted_students = {k: v for k, v in sorted(students.items(), key = lambda item: item[1], reverse = True)}  
#print sorted values   
for (key,value) in sorted_students.items():
    print(key, value)
    
print("\n")

#Grades---Extra
for (key,value) in sorted_students.items():
            if value >= 85:
                print("%s passed with A grade" % key)
            elif 70 <= value <85:
                print("%s passed with B grade" % key)
            elif 55 <= value < 70:
                print("%s passed with C grade" % key)
            elif 45 <= value < 55:
                print("%s passed with D Grade" % key)
            else:
                print("%s failed" % key)    

