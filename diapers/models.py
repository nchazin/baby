from django.db import models

class Diaper(models.Model):
    change_date = models.DateTimeField('date published')
    is_wet = models.BooleanField(default=False)
    is_dirty = models.BooleanField(default=False)
    note = models.CharField(max_length=200)
    def __unicode__(self):
	typestr = ''
        if self.is_wet:
		typestr += 'Wet'
        if self.is_dirty:
		if len(typestr) != 0:
			typestr += ' '
		typestr += 'Dirty'
	return "%s: %s %s" % (self.change_date, typestr, self.note)
	

# Create your models here.
