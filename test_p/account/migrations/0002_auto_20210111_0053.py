# Generated by Django 2.2.8 on 2021-01-10 18:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
