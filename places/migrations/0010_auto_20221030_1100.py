# Generated by Django 3.2.16 on 2022-10-30 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_auto_20221027_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='placeId',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]