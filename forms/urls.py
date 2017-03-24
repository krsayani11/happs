from django.conf.urls import url
from . import views
from .views import (
	AttendeesDestroyAPIView,
	UserUpdateAPIView,)

app_name = 'forms'
urlpatterns = [
	url(r'^$', views.search),
	url(r'^(?P<pk>\d+)/destroy/$', AttendeesDestroyAPIView.as_view()),
	url(r'^(?P<user_id>\d+)/update/$', UserUpdateAPIView.as_view()),
	]