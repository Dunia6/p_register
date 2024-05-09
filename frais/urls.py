from django.urls import path
from . import views


urlpatterns = [
    path('creer_frais/<uuid:id>/', views.Creer_frais, name='creer_frais'),
]
