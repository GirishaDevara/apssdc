# Generated by Django 3.0.3 on 2020-04-27 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emp',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]