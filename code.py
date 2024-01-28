from tabulate import tabulate
import pandas as pd

def validate_marks(marks):
    while marks > 80:
        marks = float(input("Enter your marks again (out of 80): "))
    return marks

def input_student_data():
    name = input("Enter your name/roll no.: ")
    if not name:
        print("Error: Name cannot be empty. Exiting.")
        return None

    science = validate_marks(float(input("Marks scored in Science (out of 80): ")))
    sst = validate_marks(float(input("Marks scored in SST (out of 80): ")))
    cs = validate_marks(float(input("Marks scored in Computers (out of 80): ")))
    eng = validate_marks(float(input("Marks scored in English (out of 80): ")))
    math = validate_marks(float(input("Marks scored in Math (out of 80): ")))
    kannada = validate_marks(float(input("Marks scored in Kannada (out of 80): ")))
    hindi = validate_marks(float(input("Marks scored in Hindi (out of 80): ")))

    return name, science, sst, cs, eng, math, kannada, hindi

def calculate_percentage(subject_marks):
    return ((subject_marks / 80) * 100)

x = int(input("Enter the number of students: "))

for std in range(x):
    student_data = input_student_data()
    if not student_data:
        break
   
    (name, science, sst, cs, eng, math, kannada, hindi) = student_data
    ttlmrks = science + sst + cs + eng + math + kannada + hindi

    percentages = [calculate_percentage(subject) for subject in [science, sst, cs, eng, math, kannada, hindi]]
    total_percentage = calculate_percentage(ttlmrks/7)

    table_heading = [name, "Science", "SST", "CS", "English", "Math", "Kannada", "Hindi", "Total"]
    table_data = [
         ["Marks", science, sst, cs, eng, math, kannada, hindi, ttlmrks],
         ["Percentage", *percentages, total_percentage]
     ]
    table_data = [
        ["Marks", science, sst, cs, eng, math, kannada, hindi, ttlmrks],
        ["Percentage", *percentages, total_percentage]
    ]
    table=tabulate(table_data, headers=table_heading, tablefmt="fancy_grid")
    print(table)
