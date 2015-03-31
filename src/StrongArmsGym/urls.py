from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static 

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'signups.views.home', name='home'),

    url(r'^login$', 'signups.views.login', name='login'),
    url(r'^account$', 'signups.views.account_view', name='account_view'),
    url(r'^logout$', 'signups.views.logout', name='logout'),
    url(r'^logggedin$', 'signups.views.loggedin', name='loggedin'),
    url(r'^invalid$', 'signups.views.invalid', name='invalid'),
    

    url(r'^signup$', 'signups.views.signup', name='signup'),
    # url(r'^blog/', include('blog.urls')),
   	url(r'^thank-you/$', 'signups.views.thankyou', name='thankyou'),
   	url(r'^about-us/$', 'signups.views.aboutus', name='aboutus'),

    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,
						document_root=settings.STATIC_ROOT)

	urlpatterns += static(settings.MEDIA_URL,
						document_root=settings.MEDIA_ROOT)