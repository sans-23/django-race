# Generated by Django 3.1.1 on 2020-09-16 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0013_auto_20200915_0027'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quiz',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='report',
            options={'ordering': ['student']},
        ),
    ]
