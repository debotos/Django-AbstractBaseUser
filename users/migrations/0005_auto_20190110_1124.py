# Generated by Django 2.1.2 on 2019-01-10 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190110_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='count',
            field=models.PositiveSmallIntegerField(default=0, help_text='Total amount of screenshot till now', verbose_name='Total Screenshot'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='credit',
            field=models.PositiveSmallIntegerField(default=0, help_text='Amount of credit/token user have'),
        ),
    ]
