import csv

def add_student(First_Name, Last_Name, age):
    with open('student_data.csv', 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([First_Name,Last_Name,age])

def print_student_data():
    with open('student_data.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            print(row)

add_student('Joshua', 'Miller', 21)
add_student('Goha', 'Niller', 24)
print_student_data()