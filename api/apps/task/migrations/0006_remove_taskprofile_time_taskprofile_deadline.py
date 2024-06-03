# Generated by Django 5.0.6 on 2024-06-01 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_taskprofile_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskprofile',
            name='time',
        ),
        migrations.AddField(
            model_name='taskprofile',
            name='deadline',
            field=models.DateField(blank=True, null=True, verbose_name='deadline'),
        ),
    ]