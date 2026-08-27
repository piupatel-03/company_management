from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )




    