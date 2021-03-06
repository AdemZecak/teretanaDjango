# Generated by Django 3.2 on 2021-07-06 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_auto_20210706_1422'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drugi_program_cetvrtak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gif', models.ImageField(blank=True, null=True, upload_to='images/%y/cetvrtak')),
                ('vjezbe', models.CharField(max_length=200)),
                ('serije', models.IntegerField()),
                ('ponavljanja', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Drugi_program_cetvrtak',
            },
        ),
        migrations.CreateModel(
            name='Drugi_program_petak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gif', models.ImageField(blank=True, null=True, upload_to='images/%y/petak')),
                ('vjezbe', models.CharField(max_length=200)),
                ('serije', models.IntegerField()),
                ('ponavljanja', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Drugi_program_petak',
            },
        ),
        migrations.CreateModel(
            name='Drugi_program_ponedjeljak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gif', models.ImageField(blank=True, null=True, upload_to='images/%y/ponedjeljak')),
                ('vjezbe', models.CharField(max_length=200)),
                ('serije', models.IntegerField()),
                ('ponavljanja', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Drugi_program_ponedjeljak',
            },
        ),
        migrations.CreateModel(
            name='Drugi_program_srijeda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gif', models.ImageField(blank=True, null=True, upload_to='images/%y/srijeda')),
                ('vjezbe', models.CharField(max_length=200)),
                ('serije', models.IntegerField()),
                ('ponavljanja', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Drugi_program_srijeda',
            },
        ),
        migrations.CreateModel(
            name='Drugi_program_subota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gif', models.ImageField(blank=True, null=True, upload_to='images/%y/subota')),
                ('vjezbe', models.CharField(max_length=200)),
                ('serije', models.IntegerField()),
                ('ponavljanja', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Drugi_program_subota',
            },
        ),
        migrations.CreateModel(
            name='Drugi_program_utorak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gif', models.ImageField(blank=True, null=True, upload_to='images/%y/utorak')),
                ('vjezbe', models.CharField(max_length=200)),
                ('serije', models.IntegerField()),
                ('ponavljanja', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Drugi_program_utorak',
            },
        ),
        migrations.AlterField(
            model_name='prvi_program_cetvrtak',
            name='gif',
            field=models.ImageField(blank=True, null=True, upload_to='images/%y/cetvrtak'),
        ),
        migrations.AlterField(
            model_name='prvi_program_petak',
            name='gif',
            field=models.ImageField(blank=True, null=True, upload_to='images/%y/petak'),
        ),
        migrations.AlterField(
            model_name='prvi_program_ponedjeljak',
            name='gif',
            field=models.ImageField(blank=True, null=True, upload_to='images/%y/ponedjeljak'),
        ),
        migrations.AlterField(
            model_name='prvi_program_srijeda',
            name='gif',
            field=models.ImageField(blank=True, null=True, upload_to='images/%y/srijeda'),
        ),
        migrations.AlterField(
            model_name='prvi_program_subota',
            name='gif',
            field=models.ImageField(blank=True, null=True, upload_to='images/%y/subota'),
        ),
        migrations.AlterField(
            model_name='prvi_program_utorak',
            name='gif',
            field=models.ImageField(blank=True, null=True, upload_to='images/%y/utorak'),
        ),
    ]
