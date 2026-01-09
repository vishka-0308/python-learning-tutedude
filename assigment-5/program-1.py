stu_marks={"rohan":85, "sujal":90, "ankit":78, "vivek":92, "rahul":88}
while True:
    name=input("Enter student name (or 'exit' to quit): ")
    if name.lower() == 'exit':
        break
    if name in stu_marks:
        print(f"{name}'s marks: {stu_marks[name]}")
    else:
        print("Student not found.")