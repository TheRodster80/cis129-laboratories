#Jarrod Saffioti
#CIS129 Lab 11: Exercises 9.1, 9.2, and 9.3
#5/7/2024
#These programs give info about students' grades using files.

#By the way sorry for the late submission, I was working on my calculus homework for 3 hours and ran into more of my own syntax errors than I expected

import csv

#9.1

#Open grade file, iterate through it 5 times, collect user input, and write it to the file
with open('grades.txt', mode='w') as file: 
     for grades in range(5): 
         grade = input('Please enter your grades\n') 
         file.write(f'{grade}\n') 





#9.2
         
#Open grade file, go through the lines and store the grades, calculate the average, and then display the average to the user
with open('grades.txt', mode='r') as file:
    grades = file.readlines()
    grades = [int(grade.strip()) for grade in grades]
    averageGrade = sum(grades)/len(grades)
    print(f'There are {len(grades)} grades, adding up to {sum(grades)}. The average grade is {averageGrade}')





#9.3
    
#Open grade file, collect the student's name and grades, and then write it to the file
with open('grades.csv', mode='a') as file:
    firstname = input("Please enter the student's first name: ")
    lastname = input("Please enter their last name: ")
    exam1grade = input("Their first exam score: ")
    exam2grade = input("Their second exam score: ")
    exam3grade = input("Their third exam score: ")
    writer = csv.DictWriter(file, fieldnames=["firstname", "lastname", "exam1grade", "exam2grade", "exam3grade"])
    writer.writerow({"firstname": firstname, "lastname": lastname, "exam1grade":exam1grade, "exam2grade":exam2grade, "exam3grade":exam3grade})
