"""
Project Name : Student Marks Analysis System
Language     : Python
Library      : NumPy
Author       : A. Venkata Mahalakshmi
Description  : This project analyzes student marks and generates useful statistics.
"""
#Import Numpy library
import numpy as np
#store student marks
student_marks = []
#Get number of student
number_of_students = int(input("Enter the number of students: "))
marks = np.array(student_marks)
for i in range(number_of_students):

    while True:
        mark = int(input(f"Enter marks of Student {i+1}: "))

        if 0 <= mark <= 100:
            student_marks.append(mark)
            break
        else:
            print("Please enter marks between 0 and 100.")
marks = np.array(student_marks)
print("\nStudent Marks:")
for i, mark in enumerate(marks, start=1):
    print(f"Student {i}: {mark}")
print("\n" + "=" * 50)
print("      STUDENT MARKS ANALYSIS REPORT")
print("=" * 50)
print(f"Marks: {marks}")
avg=np.mean(marks)
highest=np.max(marks)
lowest=np.min(marks)
total=np.sum(marks)
print(f"\nTotal Marks: {total}")
print(f"Average Marks: {avg}")
print(f"Highest Marks: {highest}")
print(f"Lowest Marks: {lowest}")

passing_marks=35
passed_students=np.sum(marks>=passing_marks)
failed_students=np.sum(marks<passing_marks)
print("\nPass or Fail Analysis")
print(f"Passed Students: {passed_students}")
print(f"Failed Students: {failed_students}")

sorted_marks=np.sort(marks)
print("\nTop 3 Marks:")
print(sorted_marks[-3:])
print(f"Average Marks: {avg:.2f}")
below_average = marks[marks < avg]
print(below_average)
total_students = len(marks)
pass_percentage = (passed_students / total_students) * 100
print(f"Pass Percentage: {pass_percentage:.2f}%")
print("=" * 50)