# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import members.models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_auto_20160403_1233'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cane',
            options={'ordering': ['id'], 'verbose_name': 'Bast\xf3n', 'verbose_name_plural': 'Bastones'},
        ),
        migrations.AlterModelOptions(
            name='disability',
            options={'ordering': ['name'], 'verbose_name': 'Discapacidad', 'verbose_name_plural': 'Discapacidades'},
        ),
        migrations.AlterModelOptions(
            name='house',
            options={'verbose_name': 'Vivienda', 'verbose_name_plural': 'Viviendas'},
        ),
        migrations.AlterModelOptions(
            name='member',
            options={'ordering': ['-id'], 'verbose_name': 'Miembro', 'verbose_name_plural': 'Miembros'},
        ),
        migrations.AlterModelOptions(
            name='memberfamily',
            options={'verbose_name': 'Familiar de miembro', 'verbose_name_plural': 'Familiares de miembros'},
        ),
        migrations.AlterModelOptions(
            name='occupation',
            options={'ordering': ['name'], 'verbose_name': 'Ocupaci\xf3n', 'verbose_name_plural': 'Ocupaciones'},
        ),
        migrations.AlterField(
            model_name='cane',
            name='name',
            field=models.PositiveIntegerField(verbose_name='n\xfamero de bast\xf3n'),
        ),
        migrations.AlterField(
            model_name='disability',
            name='name',
            field=models.CharField(unique=True, max_length=40, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='house',
            name='ceiling',
            field=models.ForeignKey(verbose_name='techo', to='housing.HouseMaterialCeiling', help_text='Seleccione techo'),
        ),
        migrations.AlterField(
            model_name='house',
            name='floor',
            field=models.ForeignKey(verbose_name='piso', to='housing.HouseMaterialFloor', help_text='Seleccionar piso'),
        ),
        migrations.AlterField(
            model_name='house',
            name='property_type',
            field=models.ForeignKey(verbose_name='Tipo de propiedad', to='housing.PropertyType', help_text='Seleccione el tipo de propiedad'),
        ),
        migrations.AlterField(
            model_name='house',
            name='wall',
            field=models.ForeignKey(verbose_name='pared', to='housing.HouseMaterialWall', help_text='Seleccione pared'),
        ),
        migrations.AlterField(
            model_name='member',
            name='academic_level',
            field=models.ForeignKey(verbose_name='nivel acad\xe9mico', to='commons.AcademicLevel', help_text='Seleccione nivel acad\xe9mico'),
        ),
        migrations.AlterField(
            model_name='member',
            name='cane_number',
            field=models.ForeignKey(verbose_name='n\xfamero de bast\xf3n', to='members.Cane'),
        ),
        migrations.AlterField(
            model_name='member',
            name='currently_works',
            field=models.BooleanField(default=False, help_text='Indique si actualmente tiene trabajo', verbose_name='trabaja actualmente'),
        ),
        migrations.AlterField(
            model_name='member',
            name='disabilities',
            field=models.ManyToManyField(to='members.Disability', verbose_name='discapacidades'),
        ),
        migrations.AlterField(
            model_name='member',
            name='is_mother',
            field=models.BooleanField(default=False, help_text='Indica si la miembro es madre', verbose_name='Es madre'),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_number',
            field=models.IntegerField(default=members.models.number, unique=True, verbose_name='n\xfamero de miembro'),
        ),
        migrations.AlterField(
            model_name='member',
            name='observations',
            field=models.TextField(help_text='Escribir observaciones adicionales', null=True, verbose_name='observaciones', blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='occupation',
            field=models.ForeignKey(blank=True, to='members.Occupation', help_text='Seleccione ocupaci\xf3n', null=True, verbose_name='ocupaci\xf3n'),
        ),
        migrations.AlterField(
            model_name='member',
            name='where_work',
            field=models.CharField(help_text='Empres o lugar donde trabaja', max_length=100, null=True, verbose_name='donde trabaja', blank=True),
        ),
        migrations.AlterField(
            model_name='occupation',
            name='name',
            field=models.CharField(unique=True, max_length=40, verbose_name='nombre'),
        ),
    ]
