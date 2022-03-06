from . import views
from django.urls import path
from django.conf.urls import url


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    url(r'^search/$', views.search, name='search'),
]
