# Generated by Django 2.2.24 on 2021-09-24 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ClockedTask",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("project_id", models.IntegerField(help_text="计划任务所属项目 ID")),
                ("task_id", models.IntegerField(help_text="任务 ID", null=True)),
                ("task_name", models.CharField(help_text="任务名称", max_length=128)),
                ("template_id", models.IntegerField(help_text="任务模版 ID")),
                ("template_name", models.CharField(help_text="流程名称", max_length=128)),
                (
                    "template_source",
                    models.CharField(
                        choices=[("project", "项目流程"), ("common", "公共流程"), ("onetime", "一次性任务")],
                        default="project",
                        help_text="流程模板来源",
                        max_length=32,
                    ),
                ),
                ("clocked_task_id", models.IntegerField(help_text="计划任务 Celery任务 ID", null=True)),
                ("creator", models.CharField(help_text="计划任务创建人", max_length=32)),
                ("plan_start_time", models.DateTimeField(help_text="计划任务启动时间")),
                ("task_params", models.TextField(help_text="任务创建相关数据", null=True)),
            ],
            options={"verbose_name": "计划任务", "verbose_name_plural": "计划任务", "ordering": ["-id"],},
        ),
    ]
