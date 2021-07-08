# Generated by Django 3.2 on 2021-07-01 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_alter_placanje_kategorije'),
    ]

    operations = [
        migrations.CreateModel(
            name='Placanje_sest_mjeseci',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naslov', models.CharField(max_length=200)),
                ('cijena', models.IntegerField()),
                ('kategorije', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Placanje_sest_mjeseci',
            },
        ),
    ]
