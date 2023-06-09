# Generated by Django 3.2.12 on 2022-06-01 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clocked_task", "0003_auto_20211115_1511"),
    ]

    operations = [
        migrations.AddField(
            model_name="clockedtask",
            name="create_time",
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name="创建任务时间"),
        ),
        migrations.AddField(
            model_name="clockedtask",
            name="edit_time",
            field=models.DateTimeField(auto_now=True, null=True, verbose_name="更新任务时间"),
        ),
        migrations.AddField(
            model_name="clockedtask",
            name="editor",
            field=models.CharField(default="", max_length=32, verbose_name="更新者"),
        ),
    ]
