# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-16 03:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cmdb', '0002_auto_20171011_0638'),
    ]

    operations = [
        migrations.CreateModel(
            name='PollingJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=255, verbose_name='巡检名称')),
                ('report_template', models.FileField(null=True, upload_to='./scripts/', verbose_name='巡检模板')),
            ],
            options={
                'verbose_name_plural': '巡检类型',
                'verbose_name': '巡检类型',
            },
        ),
        migrations.CreateModel(
            name='PollingJobHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('report_template', models.FileField(null=True, upload_to='./scripts/', verbose_name='巡检结果')),
                ('hosts', models.ManyToManyField(to='cmdb.Host', verbose_name='目标主机')),
            ],
            options={
                'verbose_name_plural': '执行记录',
                'verbose_name': '执行记录',
            },
        ),
        migrations.CreateModel(
            name='PollingScript',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=255, verbose_name='任务名称')),
                ('tool_script', models.TextField(verbose_name='脚本')),
                ('tool_run_type', models.IntegerField(choices=[(0, 'SaltState'), (1, 'Shell'), (2, 'PowerShell'), (3, 'Python'), (4, 'Salt命令'), (5, 'Windows批处理')], default=0, verbose_name='脚本类型')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='工具说明')),
                ('order', models.PositiveIntegerField()),
                ('polling_job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ops_polling.PollingJob', verbose_name='巡检任务')),
            ],
            options={
                'verbose_name_plural': '步骤',
                'verbose_name': '步骤',
            },
        ),
        migrations.AddField(
            model_name='pollingjobhistory',
            name='polling_job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ops_polling.PollingScript', verbose_name='巡检任务'),
        ),
    ]
