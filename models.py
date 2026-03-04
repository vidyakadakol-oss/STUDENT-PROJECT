from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name