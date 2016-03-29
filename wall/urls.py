from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^enter/', views.wall),
    url(r'^asdfasdf/$', views.create_post, name='create_post'),
    url(r'^comment/(?P<post>\d+)', views.comment, name='comment'),
]

