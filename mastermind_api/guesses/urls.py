from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from guesses import views
 
urlpatterns = [
    url(r'^guesses/$', views.GuessesList.as_view(), name='guesses-list'),
]
