# Generated by Django 2.2.24 on 2021-11-05 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("analysis_statistics", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProjectStatisticsDimension",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("dimension_id", models.CharField(max_length=32, verbose_name="统计维度id(cmdb业务模型属性id)")),
                ("dimension_name", models.CharField(max_length=32, verbose_name="统计维度名称(cmdb业务模型属性名称)")),
            ],
            options={
                "verbose_name": "业务统计数据维度",
                "verbose_name_plural": "业务统计数据维度",
            },
        ),
        migrations.CreateModel(
            name="TaskTmplExecuteTopN",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("topn", models.IntegerField(verbose_name="流程执行次数topn")),
            ],
            options={
                "verbose_name": "流程执行次数topn统计面板配置",
                "verbose_name_plural": "流程执行次数topn统计面板配置",
            },
        ),
    ]
