# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_auto_20160611_1610'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Disability',
            new_name='Diagnosis',
        ),
        migrations.AlterModelOptions(
            name='diagnosis',
            options={'ordering': ['name'], 'verbose_name': 'Diagnostico', 'verbose_name_plural': 'Diagnosticos'},
        ),
        migrations.RemoveField(
            model_name='member',
            name='disabilities',
        ),
        migrations.AddField(
            model_name='member',
            name='diagnosis',
            field=models.ManyToManyField(to='members.Diagnosis', verbose_name='diagnosticos'),
        ),
    ]
