# Generated by Django 3.2.10 on 2021-12-29 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0020_party_name_2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='party',
            name='name_2',
        ),
    ]
