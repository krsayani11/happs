"""happs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.conf.urls import url, include
	2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from events import views as eviews
from upload import views as uviews
from forms import views as fviews
from media import views as pviews


router = routers.DefaultRouter()
router.register(r'api/events', eviews.EventsViewSet)
router.register(r'api/images', uviews.FileUploadViewSet)
router.register(r'api/users', fviews.UserViewSet)
router.register(r'api/attendees', fviews.AttendeesViewSet)
router.register(r'api/media', pviews.MediaViewSet)
#router.register(r'api/events/(?P<slug>[\w-]+)/delete', eviews.EventDestroyAPIView.as_view())
admin.autodiscover()


urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^', include(router.urls)),
	url(r'^image/(?P<image_id>[A-Za-z0-9]+)$', eviews.get_event),
	url(r'^profile/(?P<image_id>[A-Za-z0-9]+)$', eviews.get_user),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^api/users/search/', include("forms.urls", namespace='forms-api')),
	url(r'^api/events/', include("events.urls", namespace='events-api'))
	
]

urlpatterns += staticfiles_urlpatterns()
