from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^project/', include('project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    ########## CREATE PROJECT URLS HERE ##########

    # This is where you'll create new URLs. More documentation on those here:
    # https://docs.djangoproject.com/en/dev/topics/http/urls/
    # I'd advise just copying, pasting and modifying from the documentation
    url('^$', 'responses.data.views.index', name='index'),
)
