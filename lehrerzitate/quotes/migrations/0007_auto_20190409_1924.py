# Generated by Django 2.2 on 2019-04-09 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0006_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='reason',
            field=models.TextField(max_length=700, verbose_name='Grund'),
        ),
    ]