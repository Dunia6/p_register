from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail_etudiant/<uuid:id>/', views.etudiant_detail, name='detail_etudiant')
]
