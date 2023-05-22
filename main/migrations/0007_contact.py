# Generated by Django 4.2 on 2023-04-25 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('massage', models.TextField()),
                ('sent', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
