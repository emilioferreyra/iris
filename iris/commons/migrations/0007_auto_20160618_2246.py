# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0006_auto_20160611_1403'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='academiclevel',
            options={'ordering': ['id'], 'verbose_name': 'Nivel acad\xe9mico', 'verbose_name_plural': 'Niveles acad\xe9micos'},
        ),
        migrations.AlterModelOptions(
            name='documenttype',
            options={'ordering': ['id'], 'verbose_name': 'Tipo de documento', 'verbose_name_plural': 'Tipos de documentos'},
        ),
    ]
