from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address= models.TextField(blank=True, null=True)
    hire_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name