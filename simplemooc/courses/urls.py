from django.contrib import admin
from django.urls import path
from simplemooc.courses import views

urlpatterns = [
    path('', views.index, name='courses.index'),
    path('<int:pk>/', views.details, name='courses.details'),

]
