from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static 

from django.contrib import admin
admin.autodiscover()

from .views import UserProfileView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'signups.views.home', name='home'),
   
    url(r'^register$', 'signups.views.register', name='register'),
    url(r'^login$', 'StrongArmsGym.views.user_login', name='login'),
    url(r'^restricted$', 'StrongArmsGym.views.restricted', name='restricted'),
    url(r'^logout$', 'StrongArmsGym.views.user_logout', name='logout'),
    # url(r'^blog/', include('blog.urls')),
   	url(r'^thank-you/$', 'signups.views.thankyou', name='thankyou'),
   	url(r'^about-us/$', 'signups.views.aboutus', name='aboutus'),
    url(r'^@(?P<user>[\w-]+)$', UserProfileView.as_view(), name="user_profile_view"),
    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,
						document_root=settings.STATIC_ROOT)

	urlpatterns += static(settings.MEDIA_URL,
						document_root=settings.MEDIA_ROOT)