from django.db import models

class Diaper(models.Model):
    change_date = models.DateTimeField('date published')
    change_type = models.CharField(max_length=1)
    note = models.CharField(max_length=200)
    def __unicode__:
	

# Create your models here.
