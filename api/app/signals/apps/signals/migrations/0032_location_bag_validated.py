# Generated by Django 2.1.5 on 2019-01-23 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signals', '0031_auto_20190130_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='bag_validated',
            field=models.BooleanField(default=False),
        ),
    ]
