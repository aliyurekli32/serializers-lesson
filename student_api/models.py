from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.number}---/---{self.first_name}"

#blank = true for admin dashboard
# null = True for DB side
