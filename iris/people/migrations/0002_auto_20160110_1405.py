# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0002_auto_20160110_1405'),
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='kinship',
            field=models.ForeignKey(to='commons.Kinship', null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='document_id',
            field=models.CharField(help_text=b'000-0000000-0', max_length=22, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='document_type',
            field=models.ForeignKey(to='commons.DocumentType', null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='person_type',
            field=models.CharField(max_length=1, null=True, choices=[(b'E', b'Employee'), (b'M', b'Member'), (b'D', b'Doctor'), (b'S', b'Supplier'), (b'K', b'Kinsman')]),
        ),
    ]
