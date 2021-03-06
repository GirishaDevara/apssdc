# Generated by Django 3.0.3 on 2020-05-12 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('emailId', models.EmailField(max_length=254, null=True)),
                ('phoneNo', models.CharField(max_length=10)),
                ('age', models.IntegerField(null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('FeMale', 'FeMale')], max_length=10)),
                ('date_of_birth', models.DateField(null=True)),
            ],
        ),
    ]
