from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Create a many-to-many relationship between students and teachers
Student.teachers = models.ManyToManyField(Teacher)
Teacher.students = models.ManyToManyField(Student)
