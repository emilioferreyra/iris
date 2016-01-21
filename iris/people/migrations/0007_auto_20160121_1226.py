# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import audit_log.models.fields
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('people', '0006_auto_20160120_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False),
        ),
        migrations.AddField(
            model_name='person',
            name='created_by',
            field=audit_log.models.fields.CreatingUserField(related_name='created_people_person_set', editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='created by'),
        ),
        migrations.AddField(
            model_name='person',
            name='created_with_session_key',
            field=audit_log.models.fields.CreatingSessionKeyField(max_length=40, null=True, editable=False),
        ),
        migrations.AddField(
            model_name='person',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False),
        ),
        migrations.AddField(
            model_name='person',
            name='modified_by',
            field=audit_log.models.fields.LastUserField(related_name='modified_people_person_set', editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='modified by'),
        ),
        migrations.AddField(
            model_name='person',
            name='modified_with_session_key',
            field=audit_log.models.fields.LastSessionKeyField(max_length=40, null=True, editable=False),
        ),
    ]
