from django.urls import path
from appinicio import views

urlpatterns = [
    path('', views.inicio),
    path('template1/<str:nombre>/<str:apellido>', views.template1),
    path('template2/<str:nombre>/<str:apellido>', views.template2),
    path('autos/crear/<str:marca>/<str:modelo>', views.crear_auto),
]


