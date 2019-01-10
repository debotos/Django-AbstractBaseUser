# Generated by Django 2.1.2 on 2019-01-10 09:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('credit_request', '0002_creditrequestmodel_req_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='creditrequestmodel',
            options={'verbose_name': 'Credit Request', 'verbose_name_plural': 'List Of All Credit Request'},
        ),
        migrations.AlterField(
            model_name='creditrequestmodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
