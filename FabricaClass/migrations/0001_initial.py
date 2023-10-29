# Generated by Django 4.2.5 on 2023-10-29 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Curso",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(blank=True, max_length=255, null=True)),
                ("turno", models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Turma",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(blank=True, max_length=10, null=True)),
                (
                    "curso",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="curso",
                        to="FabricaClass.curso",
                    ),
                ),
            ],
        ),
    ]
