# Generated by Django 2.0.5 on 2018-05-04 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='text',
            field=models.TextField(),
        ),
    ]
