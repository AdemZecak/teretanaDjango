# Generated by Django 3.2 on 2021-07-06 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_cetvrti_program_cetvrtak_cetvrti_program_petak_cetvrti_program_ponedjeljak_cetvrti_program_srijeda_c'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program_yoga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gif', models.ImageField(blank=True, null=True, upload_to='images/%y/ponedjeljak')),
                ('vjezbe', models.CharField(max_length=200)),
                ('serije', models.IntegerField()),
                ('ponavljanja', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Program_yoga',
            },
        ),
    ]
