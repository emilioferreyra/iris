# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0001_initial'),
        ('members', '0003_auto_20160110_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberAdditionalField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('observations', models.TextField()),
                ('cane_number', models.ForeignKey(to='members.Cane')),
                ('disabilities', models.ManyToManyField(to='members.Disability')),
                ('member_name', models.OneToOneField(to='members.Member')),
                ('property_type', models.ForeignKey(to='housing.PropertyType')),
            ],
            options={
                'db_table': 'members_member_additional_fields',
                'verbose_name': 'Member Additional Field',
                'verbose_name_plural': 'Member Additional Fields',
            },
        ),
    ]
