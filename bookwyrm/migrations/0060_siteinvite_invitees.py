# Generated by Django 3.1.6 on 2021-04-02 00:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookwyrm", "0059_user_preferred_timezone"),
    ]

    operations = [
        migrations.AddField(
            model_name="siteinvite",
            name="invitees",
            field=models.ManyToManyField(
                related_name="invitees", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
