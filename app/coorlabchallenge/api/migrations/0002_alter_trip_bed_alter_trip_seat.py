# Generated by Django 4.2.4 on 2024-03-24 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='bed',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='seat',
            field=models.CharField(max_length=3, null=True),
        ),
    ]