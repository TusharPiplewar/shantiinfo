from django.db import models

# Create your models here.
class task(models.Model):
    GENRE_CHOICES = [
        ('step_1', 'Step 1'),
        ('Step_2', 'Step 2'),
        ('step_3', 'Step 3'),
        ('step_4', 'Step 4'),
    ]
    task_reason =models.CharField(max_length=200)
    task_step = models.CharField(max_length=50,choices=GENRE_CHOICES)
    created_date = models.DateTimeField(auto_now_add=True)
    # task_date = models.DateField