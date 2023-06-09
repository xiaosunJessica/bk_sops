# Generated by Django 3.2.12 on 2022-06-29 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taskflow3", "0021_auto_20220523_1521"),
    ]

    operations = [
        migrations.CreateModel(
            name="TaskCallBackRecord",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False, verbose_name="ID")),
                ("task_id", models.BigIntegerField(db_index=True, verbose_name="任务ID")),
                ("url", models.TextField(verbose_name="回调地址")),
                ("create_time", models.DateTimeField(auto_now_add=True, verbose_name="创建时间")),
                (
                    "status",
                    models.CharField(
                        choices=[("ready", "未回调"), ("success", "回调成功"), ("fail", "回调失败")],
                        default="ready",
                        max_length=100,
                        verbose_name="状态",
                    ),
                ),
                ("extra_info", models.TextField(default="{}", verbose_name="附加信息")),
                ("callback_time", models.DateTimeField(blank=True, null=True, verbose_name="回调时间")),
            ],
            options={"verbose_name": "任务回调记录", "verbose_name_plural": "任务回调记录", "ordering": ["-id"],},
        ),
    ]
