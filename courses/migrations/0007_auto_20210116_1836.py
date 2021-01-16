# Generated by Django 3.1.5 on 2021-01-16 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_currencyvalue_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.CharField(max_length=256),
        ),
    ]