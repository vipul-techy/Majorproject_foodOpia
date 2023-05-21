# Generated by Django 4.1.2 on 2023-04-28 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_rename_full_tavadhosa_masaladhosa_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='registerResturant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurantName', models.CharField(max_length=50)),
                ('ownerName', models.CharField(max_length=50)),
                ('GSTNumber', models.CharField(max_length=50)),
                ('FSSAINumber', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=50)),
                ('PhoneNo', models.CharField(max_length=50)),
                ('UserName', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
            ],
        ),
    ]
