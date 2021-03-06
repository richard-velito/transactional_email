# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-04 19:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('email_rest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('is_html', models.IntegerField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='attachments',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='email_rest.Email'),
        ),
    ]
