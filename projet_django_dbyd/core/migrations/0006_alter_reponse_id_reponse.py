# Generated by Django 4.2.6 on 2023-11-06 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_alter_autresymptome_duree_douleur_thoracique_en_min_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reponse",
            name="id_reponse",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]