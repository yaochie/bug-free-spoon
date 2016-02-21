# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attrs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=20, choices=[(b'a', '10 minutes'), (b'b', '30 minutes'), (b'c', '1 hour'), (b'd', '2 hours'), (b'e', '3 hours'), (b'f', '4 hours'), (b'g', '5 hours'), (b'h', '6 hours'), (b'i', '7+ hours')])),
                ('travel', models.CharField(max_length=20, choices=[(b'w', 'Walk'), (b'p', 'Bus/Tram'), (b'c', 'Car'), (b'm', 'Train'), (b'l', 'Plane')])),
            ],
        ),
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('travel', models.CharField(max_length=20, choices=[(b'w', 'Walk'), (b'p', 'Bus/Tram'), (b'c', 'Car'), (b'm', 'Train'), (b'l', 'Plane')])),
                ('recom', models.TextField(max_length=10, choices=[(b'y', 'yes'), (b'n', 'no')])),
            ],
        ),
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=20, choices=[(b'b', 'Breakfast'), (b'l', 'Lunch'), (b't', 'Tea'), (b'd', 'Dinner'), (b's', 'Supper'), (b'n', 'Snack')])),
                ('time', models.CharField(max_length=20, choices=[(b'a', '10 minutes'), (b'b', '30 minutes'), (b'c', '1 hour'), (b'd', '2 hours'), (b'e', '3 hours'), (b'f', '4 hours'), (b'g', '5 hours'), (b'h', '6 hours'), (b'i', '7+ hours')])),
                ('travel', models.CharField(max_length=20, choices=[(b'w', 'Walk'), (b'p', 'Bus/Tram'), (b'c', 'Car'), (b'm', 'Train'), (b'l', 'Plane')])),
                ('desc', models.CharField(max_length=200)),
                ('recomm', models.TextField(max_length=10, choices=[(b'y', 'yes'), (b'n', 'no')])),
                ('parent', models.ForeignKey(to='maketrip.Itinerary')),
            ],
        ),
        migrations.AddField(
            model_name='hotels',
            name='parent',
            field=models.ForeignKey(to='maketrip.Itinerary'),
        ),
        migrations.AddField(
            model_name='attrs',
            name='parent',
            field=models.ForeignKey(to='maketrip.Itinerary'),
        ),
    ]
