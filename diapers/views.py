from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from django.template import RequestContext, loader
from django.shortcuts import render
from django.core.urlresolvers import reverse
import time
import datetime 
from .models import Diaper


# Create your views here.
def index(request):
    today = datetime.datetime.today()
    datestr = request.GET.get('date',  '%s-%s-%s' % (today.year, today.month, today.day))
    (year,month,day) = datestr.split('-')
    tmp = datetime.datetime(int(year),int(month),int(day))
    prevdate = tmp - datetime.timedelta(days=1)
    nextdate = tmp + datetime.timedelta(days=1)
    prevstr = "%s-%s-%s" % (prevdate.year, prevdate.month, prevdate.day)
    nextstr = ''
    if (nextdate <= today):
    	nextstr = "%s-%s-%s" % (nextdate.year, nextdate.month, nextdate.day)
    diapers_today = Diaper.objects.filter(change_date__year=year, 
                                          change_date__month=month,
                                          change_date__day=day)
    diapers_wet = 0
    diapers_dirty = 0
    for diaper in diapers_today:
        if diaper.is_wet:
            diapers_wet += 1
        if diaper.is_dirty:
            diapers_dirty += 1
    template = loader.get_template('diapers/index.html')
    context = RequestContext(request, {
	'diaper_list': diapers_today,
        'diapers_wet': diapers_wet,
        'diapers_dirty' : diapers_dirty,
        'date_str': datestr,
        'prevstr': prevstr,
        'nextstr':nextstr,
    })
    return HttpResponse(template.render(context))

def add(request):
    posties = request.POST
    error_code = ""
    if not posties.has_key('change_time'):
	# error here
        error_code += " missing date "
    if not posties.has_key("diaper_type_wet") and not posties.has_key("diaper_type_dirty"):
        error_code += " missing type "
    if (error_code != ""):
	#redicect...
        return render(request, 'diapers/add.html', {
            'error_message': error_code
        })
    
    change_timestruct = time.strptime(posties['change_time'], "%Y-%m-%d %H:%M")
    change_time = datetime.datetime(change_timestruct[0], change_timestruct[1],
	change_timestruct[2], change_timestruct[3], change_timestruct[4])
    wet = posties.has_key("diaper_type_wet")
    dirty = posties.has_key("diaper_type_dirty")
    for (k,v) in posties.iteritems():
	print "%s -> %s" % (k,v)
    print("string: %s - TS: %s -  time: %s" % (posties['change_time'], change_timestruct, change_time))
    print("wet: %d  dirty: %d" %(wet, dirty)) 
    new_diaper = Diaper(change_date = change_time, is_wet = wet, is_dirty = dirty)
    new_diaper.save()
    return HttpResponseRedirect(reverse('diapers:index'))
