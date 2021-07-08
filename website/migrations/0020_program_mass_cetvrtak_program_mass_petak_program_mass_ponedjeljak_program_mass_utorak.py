# Generated by Django 3.2 on 2021-07-07 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_remove_program_yoga_serije'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program_mass_cetvrtak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gif', models.ImageField(blank=True, null=True, upload_to='images/%y/mass/cetvrtak')),
                ('vjezbe', models.CharField(max_length=200)),
                ('serije', models.IntegerField()),
                ('ponavljanja', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Program_mass_cetvrtak',
            },
        ),
        migrations.CreateModel(
            name='Program_mass_petak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gif', models.ImageField(blank=True, null=True, upload_to='images/%y/mass/petak')),
                ('vjezbe', models.CharField(max_length=200)),
                ('serije', models.IntegerField()),
                ('ponavljanja', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Program_mass_petak',
            },
        ),
        migrations.CreateModel(
            name='Program_mass_ponedjeljak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gif', models.ImageField(blank=True, null=True, upload_to='images/%y/mass/ponedjeljak')),
                ('vjezbe', models.CharField(max_length=200)),
                ('serije', models.IntegerField()),
                ('ponavljanja', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Program_mass_ponedjeljak',
            },
        ),
        migrations.CreateModel(
            name='Program_mass_utorak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gif', models.ImageField(blank=True, null=True, upload_to='images/%y/mass/utorak')),
                ('vjezbe', models.CharField(max_length=200)),
                ('serije', models.IntegerField()),
                ('ponavljanja', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Program_mass_utorak',
            },
        ),
    ]
