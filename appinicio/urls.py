from django.urls import path
from appinicio import views

urlpatterns = [
    path('', views.inicio, name= "inicio"),
    path('aboutme/', views.aboutme, name='aboutme'),
    path('autos/', views.autos, name='autos'),
    path('autos/crear/', views.crear_auto, name='crear_auto'),
    path('autos/eliminar/<int:id>/', views.eliminar_auto, name='eliminar_auto'),
    path('autos/editar/<int:id>/', views.editar_auto, name='editar_auto'),
    path('autos/<int:id>/', views.ver_auto, name='ver_auto'),

]


