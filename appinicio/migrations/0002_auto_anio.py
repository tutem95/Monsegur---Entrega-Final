# Generated by Django 5.0.6 on 2024-07-12 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appinicio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='anio',
            field=models.IntegerField(default=2010),
        ),
    ]
