from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    