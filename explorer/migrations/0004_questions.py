# Generated by Django 3.0.4 on 2020-06-22 15:10

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0003_remove_post_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(blank=True, max_length=255, null=True)),
                ('Last_Name', models.CharField(blank=True, max_length=255, null=True)),
                ('Subject', models.CharField(blank=True, max_length=255, null=True)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
            ],
        ),
    ]
