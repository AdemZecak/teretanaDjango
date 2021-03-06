# Generated by Django 3.2 on 2021-07-07 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_program_mass2_cetvrtak_program_mass2_petak_program_mass2_ponedjeljak_program_mass2_utorak'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program_snaga_petak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gif', models.ImageField(blank=True, null=True, upload_to='images/%y/snaga/petak')),
                ('vjezbe', models.CharField(max_length=200)),
                ('serije', models.IntegerField()),
                ('ponavljanja', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Program_snaga_petak',
            },
        ),
        migrations.CreateModel(
            name='Program_snaga_ponedjeljak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gif', models.ImageField(blank=True, null=True, upload_to='images/%y/snaga/ponedjeljak')),
                ('vjezbe', models.CharField(max_length=200)),
                ('serije', models.IntegerField()),
                ('ponavljanja', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Program_snaga_ponedjeljak',
            },
        ),
        migrations.CreateModel(
            name='Program_snaga_srijeda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gif', models.ImageField(blank=True, null=True, upload_to='images/%y/snaga/srijeda')),
                ('vjezbe', models.CharField(max_length=200)),
                ('serije', models.IntegerField()),
                ('ponavljanja', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Program_snaga_srijeda',
            },
        ),
    ]
