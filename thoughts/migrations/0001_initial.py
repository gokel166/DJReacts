# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 21:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Thought',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('condition', models.IntegerField(choices=[(1, 'Happy'), (2, 'Satisfactory'), (3, 'Okay'), (4, 'Mad'), (5, 'Confused')])),
                ('notes', models.TextField(blank=True, default='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thoughts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
