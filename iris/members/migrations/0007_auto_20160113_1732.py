# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0003_auto_20160113_1732'),
        ('members', '0006_auto_20160112_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('house_material', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'house_part', to='housing.HouseMaterial', chained_field=b'house_part')),
                ('house_part', models.ForeignKey(to='housing.HousePart')),
                ('member_name', models.ForeignKey(to='members.Member')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='housing',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='housing',
            name='house_material',
        ),
        migrations.RemoveField(
            model_name='housing',
            name='house_part',
        ),
        migrations.RemoveField(
            model_name='housing',
            name='member_name',
        ),
        migrations.DeleteModel(
            name='Housing',
        ),
        migrations.AlterUniqueTogether(
            name='house',
            unique_together=set([('member_name', 'house_part')]),
        ),
    ]
