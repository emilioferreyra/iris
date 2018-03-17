# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_auto_20170609_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='health_insurance',
            field=models.BooleanField(default=False, verbose_name='Seguro de Salud'),
        ),
        migrations.AlterField(
            model_name='member',
            name='diagnosis',
            field=models.ManyToManyField(to='members.Diagnosis', verbose_name='Diagnosticos'),
        ),
        migrations.AlterField(
            model_name='member',
            name='observations',
            field=models.TextField(help_text='Escribir observaciones adicionales', null=True, verbose_name='Observaciones', blank=True),
        ),
        migrations.RemoveField(
            model_name='member',
            name='occupation',
        ),
        migrations.AddField(
            model_name='member',
            name='occupation',
            field=models.ManyToManyField(help_text='Seleccione ocupaci\xf3n', to='members.Occupation', null=True, verbose_name='Ocupaci\xf3n(es)', blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='where_work',
            field=models.CharField(help_text='Empresa o lugar donde trabaja', max_length=100, null=True, verbose_name='Donde trabaja', blank=True),
        ),
    ]
