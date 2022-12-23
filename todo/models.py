from django.db import models

# Create your models here.
class todo_list(models.Model):
    name = models.CharField(max_length=500)
    date = models.DateField()

    def __str__(self):
        return self.name
