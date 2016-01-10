# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
        ('housing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cane',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cane', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Disability',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=40)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Disabilities',
            },
        ),
        migrations.CreateModel(
            name='Housing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('house_material', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'house_part', to='housing.HouseMaterial', chained_field=b'house_part')),
                ('house_part', models.ForeignKey(to='housing.HousePart')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
            ],
            options={
                'verbose_name': 'Member',
                'proxy': True,
                'verbose_name_plural': 'Members',
            },
            bases=('people.person',),
        ),
        migrations.CreateModel(
            name='MemberKinsman',
            fields=[
            ],
            options={
                'verbose_name': 'Member Kinsman',
                'proxy': True,
                'verbose_name_plural': 'Member Kinsmans',
            },
            bases=('people.person',),
        ),
        migrations.AddField(
            model_name='housing',
            name='member_name',
            field=models.ForeignKey(to='members.Member'),
        ),
        migrations.AlterUniqueTogether(
            name='housing',
            unique_together=set([('member_name', 'house_part')]),
        ),
    ]
