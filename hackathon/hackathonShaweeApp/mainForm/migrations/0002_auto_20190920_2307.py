# Generated by Django 2.2.5 on 2019-09-21 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainForm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='age',
            field=models.IntegerField(),
        ),
    ]
