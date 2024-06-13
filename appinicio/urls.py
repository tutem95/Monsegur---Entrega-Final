from django.urls import path
from appinicio import views

urlpatterns = [
    path('', views.inicio, name= "inicio"),
    path('template1/<str:nombre>/<str:apellido>', views.template1),
    path('template2/', views.template2, name="template2"),
    path('autos/crear/', views.crear_auto, name='crear_auto'),
]


