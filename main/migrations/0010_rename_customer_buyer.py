# Generated by Django 4.2 on 2023-05-02 11:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0009_customer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customer',
            new_name='Buyer',
        ),
    ]
