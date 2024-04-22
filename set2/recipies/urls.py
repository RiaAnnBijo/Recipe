from django.urls import path
from . import views

app_name = 'recipie'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('radmin/',views.AdminRecipies, name='radmin'),
    path('add/',views.addrecipies),
    path('user/',views.ViewRecipies, name='user'),

]