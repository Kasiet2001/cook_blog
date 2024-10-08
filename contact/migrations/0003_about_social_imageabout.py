# Generated by Django 5.1 on 2024-08-21 15:20

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_alter_contactmodel_website'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor.fields.RichTextField()),
                ('mini_text', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.FileField(upload_to='icons/')),
                ('name', models.CharField(max_length=200)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ImageAbout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about/')),
                ('alt', models.CharField(max_length=100)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='about_images', to='contact.about')),
            ],
        ),
    ]
