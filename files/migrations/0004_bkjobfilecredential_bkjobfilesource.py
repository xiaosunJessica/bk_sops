# Generated by Django 2.2.16 on 2021-07-29 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("files", "0003_uploadticket_isavailable_default_true"),
    ]

    operations = [
        migrations.CreateModel(
            name="BKJobFileCredential",
            fields=[
                ("bk_biz_id", models.IntegerField(primary_key=True, serialize=False, verbose_name="CC business id")),
                ("credential_id", models.CharField(max_length=128, verbose_name="JOB credential id")),
            ],
        ),
        migrations.CreateModel(
            name="BKJobFileSource",
            fields=[
                ("bk_biz_id", models.IntegerField(primary_key=True, serialize=False, verbose_name="CC business id")),
                ("file_source_id", models.IntegerField(verbose_name="JOB file source id")),
            ],
        ),
    ]
