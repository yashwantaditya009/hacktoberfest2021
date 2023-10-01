import csv

def read_student_data(file_name):
    student_data = []
    try:
        with open(file_name, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                student_data.append(row)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    return student_data

def calculate_average_score(student_data):
    total_score = 0
    num_students = len(student_data)

    for student in student_data:
        total_score += int(student['Score'])

    if num_students == 0:
        return 0
    else:
        return total_score / num_students

def generate_report(student_data, average_score):
    print("Student Report")
    print("-" * 40)
    print(f"Average Score: {average_score:.2f}\n")

    print("Student Details")
    print("-" * 40)
    for student in student_data:
        print(f"Name: {student['Name']}")
        print(f"Score: {student['Score']}")
        print()

if __name__ == "__main__":
    input_file_name = "student_records.csv"
    student_data = read_student_data(input_file_name)

    if student_data:
        average_score = calculate_average_score(student_data)
        generate_report(student_data, average_score)
