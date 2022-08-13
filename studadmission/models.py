from django.db import models

# Create your models here.


class StudAdmission(models.Model):
    roll_number = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    city = models.CharField(max_length=200)
    sel_class = (
        ('', 'Select Class'),
        ('1', '1st'),
        ('2', '2nd'),
        ('3', '3rd'),
        ('4', '4th'),
        ('5', '5th'),
        ('6', '6th'),
        ('7', '7th'),
        ('8', '8th'),
        ('9', '9th'),
        ('10', '10th'),
        ('11', '11th'),
        ('12', '12th'),
                 )
    std = models.CharField(max_length=200, choices=sel_class)