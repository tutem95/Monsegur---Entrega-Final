from django.urls import path
from appinicio import views

urlpatterns = [
    path('', views.inicio, name= "inicio"),
    path('autos/', views.autos, name='autos'),
    path('autos/crear/', views.crear_auto, name='crear_auto'),

]


