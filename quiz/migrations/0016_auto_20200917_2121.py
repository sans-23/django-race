# Generated by Django 3.1.1 on 2020-09-17 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0015_response'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='is_correct',
            field=models.BooleanField(default=True),
        ),
    ]
