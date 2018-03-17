# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0005_auto_20160216_0133'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='academiclevel',
            options={'verbose_name': 'Nivel acad\xe9mico', 'verbose_name_plural': 'Niveles acad\xe9micos'},
        ),
        migrations.AlterModelOptions(
            name='documenttype',
            options={'verbose_name': 'Tipo de documento', 'verbose_name_plural': 'Tipos de documentos'},
        ),
        migrations.AlterModelOptions(
            name='kinship',
            options={'ordering': ['name'], 'verbose_name': 'Parentezco', 'verbose_name_plural': 'Parentezcos'},
        ),
        migrations.AlterModelOptions(
            name='maritalstatus',
            options={'ordering': ['id'], 'verbose_name': 'Estado civil', 'verbose_name_plural': 'Estado civil'},
        ),
        migrations.AlterModelOptions(
            name='persontype',
            options={'ordering': ['id'], 'verbose_name': 'Tipo de persona', 'verbose_name_plural': 'Tipos de personas'},
        ),
        migrations.AlterModelOptions(
            name='phonetype',
            options={'ordering': ['id'], 'verbose_name': 'Tipo de tel\xe9fono', 'verbose_name_plural': 'Tipos de tel\xe9fonos'},
        ),
        migrations.AlterField(
            model_name='academiclevel',
            name='name',
            field=models.CharField(unique=True, max_length=45, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='documenttype',
            name='name',
            field=models.CharField(unique=True, max_length=20, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='kinship',
            name='name',
            field=models.CharField(unique=True, max_length=45, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='maritalstatus',
            name='name',
            field=models.CharField(unique=True, max_length=45, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='persontype',
            name='name',
            field=models.CharField(unique=True, max_length=45, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='phonetype',
            name='name',
            field=models.CharField(unique=True, max_length=45, verbose_name='nombre'),
        ),
    ]
