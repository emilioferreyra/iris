# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0006_auto_20160103_0007'),
        ('members', '0002_auto_20160102_2337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_number', localflavor.us.models.PhoneNumberField(max_length=20)),
                ('phone_type', models.ForeignKey(to='commons.PhoneType')),
            ],
        ),
        migrations.AlterModelOptions(
            name='maritalstatus',
            options={'ordering': ['id'], 'verbose_name_plural': 'Marital status'},
        ),
    ]
