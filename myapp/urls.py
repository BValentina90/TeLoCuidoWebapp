from django.urls import path
from . import views

urlpatterns = [
    path('', views.portada, name="portada"),
    path('register/', views.register, name="register"),
    path('save/<num_registro>/', views.save_register, name="save_register"),
    path('register_conductor/', views.register_conductor, name="register_conductor"),
    path('login_conductor/', views.login_conductor, name="login_conductor"),
    path('login_cuidacoches/', views.login_cuidacoches, name="login_cuidacoches"),
    path('logout/', views.logout, name="logout"),
    path('home_cuidacoches/', views.home_cuidacoches, name="home_cuidacoches"),
    path('monedero_cuidacoches/', views.monedero_cuidacoches, name="monedero_cuidacoches"),
    path('perfil_cuidacoches/', views.perfil_cuidacoches, name="perfil_cuidacoches"),
    path('home_conductor/', views.home_conductor, name="home_conductor"),
    path('rel/', views.rel, name="rel"),
    path('servicios_conductor/', views.servicios_conductor, name="servicios_conductor"),
    path('estacionado/', views.estacionado, name="estacionado"),
    path('quienes_somos/', views.quienes_somos, name="quienes_somos"),
    path('como_funciona/', views.como_funciona, name="como_funciona")
    ]