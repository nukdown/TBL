# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-30 02:41
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20171030_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(error_messages={'unique': 'A user with that email already exists.'}, help_text='Email that will be used as username.', max_length=254, unique=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Short name that will be used uniquely on the platform.', max_length=30, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$', 32), 'Enter a valid username', 'This value should only contain letters, numbers,         and characters @/./+/-/_.', 'invalid')], verbose_name='User'),
        ),
    ]
