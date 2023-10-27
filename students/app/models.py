from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\d{10}$', message="Số điện thoại phải gồm 10 chữ số.")
    phone = models.CharField(max_length=10, validators=[phone_regex], null=True)
    
    def __str__(self):
        return self.name