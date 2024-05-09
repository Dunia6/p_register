from django.urls import path
from . import views

urlpatterns = [
    path('qr_code/<uuid:id>/', views.generer_code, name='qr_code'),
    path('decode/', views.dechiffrer, name='decode'),
    path('lire_qr/', views.lire_code_qr, name='lire_qr'),
     path('scan/', views.scan_qr_code, name='scan_qr_code'),
]
