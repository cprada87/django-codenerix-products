# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-03 16:14
from __future__ import unicode_literals

import codenerix.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codenerix_products', '0029_auto_20170803_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductFinalOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('order', models.SmallIntegerField(blank=True, null=True, verbose_name='Order')),
                ('product_final', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productfinals_option', to='codenerix_products.ProductFinal', verbose_name='Product Final')),
                ('products_pack', models.ManyToManyField(related_name='productfinals_optionpack', to='codenerix_products.ProductFinal')),
            ],
            options={
                'default_permissions': ('add', 'change', 'delete', 'view', 'list'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductFinalOptionTextEN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('slug', models.CharField(max_length=250, unique=True, verbose_name='Slug')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Name')),
                ('description', codenerix.fields.WysiwygAngularField(verbose_name='Description')),
                ('product_final_option', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='en', to='codenerix_products.ProductFinalOption')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductFinalOptionTextES',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('slug', models.CharField(max_length=250, unique=True, verbose_name='Slug')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Name')),
                ('description', codenerix.fields.WysiwygAngularField(verbose_name='Description')),
                ('product_final_option', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='es', to='codenerix_products.ProductFinalOption')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
