# Generated by Django 3.2 on 2021-07-06 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_alter_program_yoga_gif'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program_yoga',
            name='serije',
        ),
    ]