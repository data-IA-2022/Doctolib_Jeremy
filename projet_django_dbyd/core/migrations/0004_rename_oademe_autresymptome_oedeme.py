# Generated by Django 4.2.6 on 2023-11-03 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_administrator_last_login"),
    ]

    operations = [
        migrations.RenameField(
            model_name="autresymptome",
            old_name="oademe",
            new_name="oedeme",
        ),
    ]
