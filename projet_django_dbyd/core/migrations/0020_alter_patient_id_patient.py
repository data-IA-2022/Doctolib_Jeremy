# Generated by Django 4.2.6 on 2023-11-16 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0019_alter_medecin_tel_medecin"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patient",
            name="id_patient",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
