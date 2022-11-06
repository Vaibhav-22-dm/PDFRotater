from rest_framework import serializers
from .models import *

class PDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDFModel
        fields = ['id', 'inputFile', 'outputFile'] 