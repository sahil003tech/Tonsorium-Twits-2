# Generated by Django 2.2.6 on 2020-03-20 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_salarie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='paid',
        ),
    ]