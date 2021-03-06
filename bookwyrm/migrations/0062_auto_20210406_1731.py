# Generated by Django 3.1.6 on 2021-04-06 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookwyrm", "0061_auto_20210402_1435"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="connector",
            name="connector_file_valid",
        ),
        migrations.AlterField(
            model_name="connector",
            name="connector_file",
            field=models.CharField(
                choices=[
                    ("openlibrary", "Openlibrary"),
                    ("inventaire", "Inventaire"),
                    ("self_connector", "Self Connector"),
                    ("bookwyrm_connector", "Bookwyrm Connector"),
                ],
                max_length=255,
            ),
        ),
    ]
