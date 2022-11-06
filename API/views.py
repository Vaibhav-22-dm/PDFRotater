from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from .models import *
import fitz
from django.core.files import File
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import *
from django.conf import settings
# Create your views here.

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def getRotatedPDF(request):
    try:
        page = request.data.get('page')
        angle = request.data.get('angle')
        file = request.FILES['file']
        print(file)
        object = PDFModel.objects.create(inputFile=file)
        object.save()
        print(f'{settings.MEDIA_ROOT}/{object.inputFile}')
        doc = fitz.open(f'{settings.MEDIA_ROOT}/{object.inputFile}')
        print(doc)
        page = doc[int(page)-1]
        page.set_rotation(int(angle))
        doc.save(f'{settings.MEDIA_ROOT}/output_files/{file}')
        object.outputFile = f'output_files/{file}'
        object.save()
        serializer = PDFSerializer(object)
        print(serializer.data)
        return Response(serializer.data, status=200)
    except Exception as e:
        return Response({'message':str(e)}, status=status.HTTP_400_BAD_REQUEST)