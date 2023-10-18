#To display the students corresponding to a teacher, we can use the following code:
def get_students(teacher):
    students = teacher.students.all()
    return students

def display_students(teacher):
    students = get_students(teacher)
    for student in students:
        print(student.name)

# Example usage:

teacher = Teacher.objects.get(id=1)
display_students(teacher)
