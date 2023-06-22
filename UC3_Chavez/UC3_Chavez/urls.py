from django.contrib import admin
from django.urls import path
from miapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', views.inicio, name="inicio"),
    path('primos/', views.primos, name="primos"),
    path('examen/', views.examen, name="examen"),
]
