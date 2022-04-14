from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.indexView, name='home'),
    path('results/', views.resultsView, name='results'),
    path('<slug:slug>/', views.ExperienceDetail.as_view(),
         name='experience_detail'),
    path('edit/<review_id>', views.edit_review, name='edit'),
    path('delete/<review_id>', views.delete_review, name='delete'),
    path('editexp/<experience_id>', views.edit_experience, name='editexp'),
    path('deleteexp/<experience_id>', views.delete_experience,
         name='deleteexp')
]
