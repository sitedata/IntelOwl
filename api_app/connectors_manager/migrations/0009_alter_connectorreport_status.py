# Generated by Django 3.2.4 on 2021-08-02 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("connectors_manager", "0008_auto_20210728_0922"),
    ]

    operations = [
        migrations.AlterField(
            model_name="connectorreport",
            name="status",
            field=models.CharField(
                choices=[
                    ("FAILED", "Failed"),
                    ("PENDING", "Pending"),
                    ("RUNNING", "Running"),
                    ("SUCCESS", "Success"),
                    ("KILLED", "Killed"),
                ],
                max_length=50,
            ),
        ),
    ]