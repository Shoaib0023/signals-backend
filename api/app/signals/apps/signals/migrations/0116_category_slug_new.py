# Generated by Django 2.2.13 on 2020-07-31 06:14

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('signals', '0115_auto_20200730_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug_new',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from=['category_level_1']),
        ),
    ]
