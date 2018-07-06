from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from game import views
 
urlpatterns = [
    url(r'^game/$', views.GameList.as_view(), name='game-list'),
    url(r'^game/(?P<pk>[0-9]+)/$', views.GameDetail.as_view(), name='game-detail'),
]
