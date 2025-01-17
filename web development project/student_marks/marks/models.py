from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=100, default='Unknown')  # Default added
    subject = models.CharField(max_length=100)
    marks = models.IntegerField()

    def __str__(self):
        return self.name
