# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0009_auto_20160122_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='doctor',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='clinic', to='doctors.DoctorAdditionalField', chained_field='clinic'),
        ),
    ]
