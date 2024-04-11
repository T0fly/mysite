from django.db import models


# Create your models here.
class Class(models.Model):
    class_name = models.CharField(max_length=10)

    def __str__(self):
        return self.class_name


class Student(models.Model):
    student_name = models.CharField(max_length=10)
    Class = models.ForeignKey(Class, on_delete=models.CASCADE)


def __str__(self):
    return f"{self.student_name} of class {self.Class}"
