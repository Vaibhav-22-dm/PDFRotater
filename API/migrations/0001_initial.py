# Generated by Django 4.1.3 on 2022-11-05 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PDFModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inputFile', models.FileField(blank=True, null=True, upload_to='media/input_files')),
                ('outputFile', models.FileField(blank=True, null=True, upload_to='media/output_files')),
            ],
        ),
    ]
