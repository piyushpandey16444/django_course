# Generated by Django 3.1.5 on 2021-01-16 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20210116_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='currencyvalue',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
