# Student Report Card

student_name = input("Enter the name of the student: ")
phy_marks = float(input("Enter the marks in Physics [out of 80]: "))
chem_marks = float(input("Enter the marks in Chemistry [out of 80]: "))
eng_marks = float(input("Enter the marks in English [out of 80]: "))

def total(phy_marks, chem_marks, eng_marks):
    return (phy_marks + chem_marks + eng_marks)

def percentage(total):
    return (total / 240) * 100

def grade(student_grade):
    if student_grade >= 90:
        print ("You got a A")
    elif student_grade <= 89 and student_grade >= 75:
        print ("You got a B")
    elif student_grade >= 50 and student_grade <= 74:
        print ("You got a C")

print (f"Name of the Student: {student_name}")

total_marks = total(phy_marks, chem_marks, eng_marks)
print (f"Total marks: {total_marks}")

percentage = percentage(total_marks)
print (f"Total Percentage: {percentage}%")

grader = grade(total_marks)



