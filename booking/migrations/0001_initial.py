# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-10 22:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book_ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('ticket_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_id', models.IntegerField()),
                ('seat_id', models.IntegerField()),
                ('aircomp', models.CharField(blank=True, default='', max_length=100)),
                ('flight_number', models.IntegerField()),
                ('price', models.IntegerField()),
                ('destination', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'ordering': ('ticket_id',),
            },
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('email', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'ordering': ('user_id',),
            },
        ),
    ]
