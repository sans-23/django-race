# Generated by Django 3.1.1 on 2020-09-18 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0021_remove_quiz_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='attempt',
            field=models.IntegerField(default=1),
        ),
    ]