# Generated by Django 4.2.6 on 2023-11-14 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "core",
            "0015_alter_activitephysique_activite_physique_journee_en_cours_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="activitephysique",
            name="activite_physique_journee_en_cours",
            field=models.IntegerField(
                blank=True, choices=[(1, "Oui"), (0, "Non")], null=True
            ),
        ),
    ]
