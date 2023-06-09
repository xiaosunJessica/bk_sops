# Generated by Django 2.2.24 on 2021-12-15 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taskflow3", "0018_auto_20211213_1554"),
    ]

    operations = [
        migrations.CreateModel(
            name="TimeoutNodesRecord",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False, verbose_name="ID")),
                ("timeout_nodes", models.TextField(verbose_name="超时节点信息")),
            ],
            options={
                "verbose_name": "超时节点数据记录 TimeoutNodesRecord",
                "verbose_name_plural": "超时节点数据记录 TimeoutNodesRecord",
            },
        ),
    ]
