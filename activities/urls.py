from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.indexView, name='home'),
    path('results/', views.resultsView, name='results'),
    path('<slug:slug>/', views.ExperienceDetail.as_view(), name='experience_detail'),
]
