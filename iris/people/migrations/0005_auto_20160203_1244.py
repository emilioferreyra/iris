# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0004_auto_20160203_1243'),
        ('people', '0004_auto_20160203_1243'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonPhone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_number', localflavor.us.models.PhoneNumberField(help_text='999-999-9999', max_length=20, null=True)),
                ('default', models.BooleanField(default=False, verbose_name='default phone')),
                ('person_name', models.ForeignKey(to='people.Person')),
                ('phone_type', models.ForeignKey(to='commons.PhoneType', null=True)),
            ],
            options={
                'db_table': 'people_person_phone',
                'verbose_name': 'Phone',
                'verbose_name_plural': 'Phones',
            },
        ),
        migrations.AlterUniqueTogether(
            name='personphone',
            unique_together=set([('person_name', 'phone_type')]),
        ),
    ]
