# Generated by Django 2.2 on 2019-04-06 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0003_quote_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='text',
            field=models.TextField(max_length=400, unique=True, verbose_name='Zitat'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(max_length=40, unique=True, verbose_name='Name'),
        ),
    ]
