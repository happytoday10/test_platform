# Generated by Django 2.1.1 on 2018-11-10 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interface_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testcase',
            name='project',
        ),
    ]
