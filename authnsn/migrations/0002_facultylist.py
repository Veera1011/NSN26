# Generated by Django 5.1.6 on 2025-03-18 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authnsn', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facultylist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('photo', models.ImageField(upload_to='faculty_photos/')),
            ],
            options={
                'verbose_name_plural': 'Faculty Members',
            },
        ),
    ]
