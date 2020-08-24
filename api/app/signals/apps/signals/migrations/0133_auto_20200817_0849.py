# Generated by Django 2.2.13 on 2020-08-17 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signals', '0132_attachment_is_issue_finish_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('orac_commment', models.CharField(max_length=200)),
                ('oracCode', models.CharField(max_length=100)),
                ('oracCategory', models.CharField(max_length=200)),
                ('oracType', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SignalCityObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('complainID', models.CharField(max_length=200)),
                ('complainIDall', models.CharField(max_length=200)),
                ('reportCount', models.CharField(max_length=200)),
                ('is_Orac', models.BooleanField(default=False)),
                ('city_obj', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='signals.CityObject')),
                ('signal_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='signals.Signal')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='signal',
            name='city_object',
            field=models.ManyToManyField(blank=True, to='signals.CityObject'),
        ),
    ]