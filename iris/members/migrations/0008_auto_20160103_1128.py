# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0001_initial'),
        ('members', '0007_auto_20160103_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Housing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('house_material', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'house_part', to='housing.HouseMaterial', chained_field=b'house_part')),
                ('house_part', models.ForeignKey(to='housing.HousePart')),
                ('member', models.ForeignKey(to='members.Member')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='housing',
            unique_together=set([('member', 'house_part')]),
        ),
    ]
