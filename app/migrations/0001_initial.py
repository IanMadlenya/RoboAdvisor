# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-15 14:00
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('symbol', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('sector', models.CharField(max_length=50)),
                ('subSector', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'asset',
            },
        ),
        migrations.CreateModel(
            name='AssetData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('price', models.FloatField()),
                ('prediction', models.FloatField(null=True)),
                ('errorMargin', models.FloatField()),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Asset')),
            ],
            options={
                'db_table': 'assetdata',
            },
        ),
        migrations.CreateModel(
            name='MinimumSpanningTreeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assetIdTwo', models.IntegerField()),
                ('slope', models.FloatField()),
                ('intercept', models.FloatField()),
                ('assetIdOne', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Asset')),
            ],
            options={
                'db_table': 'minimum_spanning_tree_model',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField()),
                ('headline', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
                ('sentiment', models.FloatField()),
            ],
            options={
                'db_table': 'news',
            },
        ),
        migrations.CreateModel(
            name='NewsGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('effect', models.FloatField()),
                ('assetId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Asset')),
            ],
            options={
                'db_table': 'news_group',
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('userId', models.IntegerField()),
            ],
            options={
                'db_table': 'portfolio',
            },
        ),
        migrations.CreateModel(
            name='PortfolioAssetMapping',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('currentCount', models.IntegerField()),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Asset')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Portfolio')),
            ],
            options={
                'db_table': 'portfolio_asset_mapping',
            },
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField()),
                ('trade', models.CharField(max_length=50)),
                ('mapping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.PortfolioAssetMapping')),
                ('recommendedAsset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Asset')),
            ],
            options={
                'db_table': 'recommendation',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastUpdateDate', models.DateTimeField()),
            ],
            options={
                'db_table': 'status',
            },
        ),
        migrations.CreateModel(
            name='TimeSeriesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coefficients', django.contrib.postgres.fields.jsonb.JSONField()),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Asset')),
            ],
            options={
                'db_table': 'timeSeries_model',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeStamp', models.DateTimeField()),
                ('trade', models.CharField(max_length=50)),
                ('initialCount', models.IntegerField()),
                ('finalCount', models.IntegerField()),
                ('tradeCount', models.IntegerField()),
                ('price', models.FloatField()),
                ('mapping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.PortfolioAssetMapping')),
            ],
            options={
                'db_table': 'transaction',
            },
        ),
        migrations.AddField(
            model_name='news',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.NewsGroup'),
        ),
    ]
