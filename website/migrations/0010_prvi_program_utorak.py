# Generated by Django 3.2 on 2021-07-06 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_alter_prvi_program_gif'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prvi_program_utorak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gif', models.ImageField(blank=True, null=True, upload_to='images/%y')),
                ('vjezbe', models.CharField(max_length=200)),
                ('serije', models.IntegerField()),
                ('ponavljanja', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Prvi_program_utorak',
            },
        ),
    ]
