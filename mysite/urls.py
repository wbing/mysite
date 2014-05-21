from django.conf.urls import patterns, include, url

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'mysite.views.home', name='home'),
     url(r'^myapp/', 'myapp.views.index', name='index'),
     url(r'^app/', include('app.urls')),

    #url(r'^admin/', include(admin.site.urls)),
)
