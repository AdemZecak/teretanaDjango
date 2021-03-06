# Generated by Django 3.2 on 2021-07-08 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0023_misicna_definicija_petak_misicna_definicija_ponedjeljak_misicna_definicija_srijeda'),
    ]

    operations = [
        migrations.CreateModel(
            name='Misicna_definicija2_petak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gif', models.ImageField(blank=True, null=True, upload_to='images/%y/definicija2/petak')),
                ('vjezbe', models.CharField(max_length=200)),
                ('serije', models.IntegerField()),
                ('ponavljanja', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Misicna_definicija2_petak',
            },
        ),
        migrations.CreateModel(
            name='Misicna_definicija2_ponedjeljak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gif', models.ImageField(blank=True, null=True, upload_to='images/%y/definicija2/ponedjeljak')),
                ('vjezbe', models.CharField(max_length=200)),
                ('serije', models.IntegerField()),
                ('ponavljanja', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Misicna_definicija2_ponedjeljak',
            },
        ),
        migrations.CreateModel(
            name='Misicna_definicija_srijeda2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gif', models.ImageField(blank=True, null=True, upload_to='images/%y/definicija2/srijeda')),
                ('vjezbe', models.CharField(max_length=200)),
                ('serije', models.IntegerField()),
                ('ponavljanja', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Misicna_definicija2_srijeda',
            },
        ),
    ]
