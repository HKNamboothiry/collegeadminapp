from django.db import models

# Create your models here.
class Student(models.Model):
    name_student = models.CharField(max_length=250)
    address = models.TextField()
    dob = models.IntegerField(default=2001)
    propic = models.ImageField(upload_to='gallery', default='')

    def __str__(self):
        return self.name_student