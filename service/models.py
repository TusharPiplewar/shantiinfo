from django.db import models

# Create your models here.
class task(models.Model):
    GENRE_CHOICES = [
        ('1', 'Step 1'),
        ('2', 'Step 2'),
        ('3', 'Step 3'),
        ('4', 'Step 4'),
    ]
    task_reason =models.CharField(max_length=200)
    task_step = models.CharField(max_length=50,choices=GENRE_CHOICES)
    created_date = models.DateTimeField(auto_now_add=True)