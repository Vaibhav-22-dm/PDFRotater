from django.db import models

# Create your models here.
class PDFModel(models.Model):
    inputFile = models.FileField(upload_to='input_files', null=True, blank=True)
    outputFile = models.FileField(upload_to='output_files', null=True, blank=True)

    def __str__(self):
        return "File-" + str(self.id)