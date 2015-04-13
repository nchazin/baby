from django.contrib import admin

from .models import Diaper

class DiaperAdmin(admin.ModelAdmin):
	fields = ['change_date', 'change_type', 'note']

admin.site.register(Diaper, DiaperAdmin)

# Register your models here.
