from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Activity(models.Model):
    
    TYPE_CHOICES = [
        ('running', 'Running'),
        ('cycling','Cycling'),
        ('swimming','Swimming'),
        ('yoga','Yoga'),
        ('gym','gym'),
        ('walking', 'Walking'),
        ('hiking', 'Hiking'),
        ('dancing', 'Dancing'),
        ('boxing', 'Boxing'),
        ('weightlifting', 'Weightlifting'),
        ('aerobics', 'Aerobics'),
        ('pilates', 'Pilates'),
        ('other', 'Other'), 
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="activities")
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    duration = models.PositiveIntegerField()
    calories = models.PositiveIntegerField()
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)


    def __str__(self):
        return f"{self.type} - {self.user.username} ({self.date})"