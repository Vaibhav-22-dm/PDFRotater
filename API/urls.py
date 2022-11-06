from django.urls import path, include
from .views import *

urlpatterns = [
    path('getrotatedpdf/', getRotatedPDF, name='get_rotated_pdf')
]