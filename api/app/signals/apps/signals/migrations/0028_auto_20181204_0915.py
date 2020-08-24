# Generated by Django 2.1.2 on 2018-12-04 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signals', '0027_SIG858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='state',
            field=models.CharField(
                blank=True,
                choices=[
                    ('m', 'Gemeld'),
                    ('i', 'In afwachting van behandeling'),
                    ('b', 'In behandeling'),
                    ('h', 'On hold'),
                    ('ready to send', 'Te verzenden naar extern systeem'),
                    ('o', 'Afgehandeld'),
                    ('a', 'Geannuleerd'),
                    ('reopened', 'Heropend'),
                    ('sent', 'Verzonden naar extern systeem'),
                    ('send failed', 'Verzending naar extern systeem mislukt'),
                    ('done external', 'Melding is afgehandeld in extern systeem')
                ],
                default='m',
                help_text='Melding status',
                max_length=20
            ),
        ),
    ]
