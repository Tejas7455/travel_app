from django.db import models
CHOICES= (
    ('beach','Beach'),
    ('mountain','Mountain'),
    ('city','City'),
    ('historical','Historical'),
)

class Destination(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    description = models.TextField()
    best_time_to_visit = models.CharField(max_length=40)
    category = models.CharField(max_length=20, choices=CHOICES)
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.name}'