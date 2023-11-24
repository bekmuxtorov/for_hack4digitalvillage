# Generated by Django 4.2 on 2023-11-24 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authtoken', '0003_tokenproxy'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TokenProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Token',
                'verbose_name_plural': 'Tokens',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('authtoken.token',),
        ),
    ]