# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_person_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='nationality',
            field=models.ForeignKey(default=21, to='location.Nationality'),
        ),
        migrations.AlterField(
            model_name='person',
            name='picture',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to=b'people_pictures', blank=True),
        ),
        migrations.AlterField(
            model_name='personaddress',
            name='country',
            field=models.ForeignKey(default=1, to='location.Country'),
        ),
    ]
