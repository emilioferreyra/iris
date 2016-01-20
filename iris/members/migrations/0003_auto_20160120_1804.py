# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20160120_1752'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ocupation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Ocupation',
                'verbose_name_plural': 'Ocupations',
            },
        ),
        migrations.AlterField(
            model_name='memberadditionalfield',
            name='ocupation',
            field=models.ForeignKey(to='members.Ocupation', null=True),
        ),
        migrations.AlterField(
            model_name='memberadditionalfield',
            name='where_work',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
