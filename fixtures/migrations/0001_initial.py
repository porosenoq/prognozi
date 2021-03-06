# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-03 22:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('match_date', models.DateTimeField(blank=True, null=True)),
                ('league', models.IntegerField(choices=[(1, 'English Premier League'), (2, 'Spanish Primera Division'), (3, 'Bulgarian A PFG')])),
                ('hometeam', models.CharField(max_length=255)),
                ('awayteam', models.CharField(max_length=255)),
                ('homecoef', models.DecimalField(decimal_places=2, max_digits=4)),
                ('xcoef', models.DecimalField(decimal_places=2, max_digits=4)),
                ('awaycoef', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
    ]
