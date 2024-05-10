# Generated by Django 4.2.5 on 2024-03-28 15:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("FabricaClass", "0005_criterios_pergunta_formulario_pergunta"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="criterios",
            name="booleano",
        ),
        migrations.RemoveField(
            model_name="criterios",
            name="numerico",
        ),
        migrations.RemoveField(
            model_name="criterios",
            name="texto",
        ),
        migrations.AddField(
            model_name="criterios",
            name="descricao",
            field=models.CharField(default="Criterio", max_length=255),
        ),
        migrations.AddField(
            model_name="criterios",
            name="valor_maximo",
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name="criterios",
            name="valor_minimo",
            field=models.IntegerField(default=1),
        ),
    ]
