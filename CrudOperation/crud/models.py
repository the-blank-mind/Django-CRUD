from django.db import models

class Employee(models.Model):
    name= models.CharField(max_length=20)
    email= models.CharField(max_length=20)
    pwd= models.CharField(max_length=20)

    def __str__(self):
        return self.name
    