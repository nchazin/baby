from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'babysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^diapers/', include('diapers.urls', namespace="diapers")),
    url(r'^$', include('diapers.urls', namespace="diapers")),
    url(r'^admin/', include(admin.site.urls)),
   
]
