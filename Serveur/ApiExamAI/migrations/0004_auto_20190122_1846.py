# Generated by Django 2.1.5 on 2019-01-22 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiExamAI', '0003_auto_20190122_1844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eleve',
            name='clee',
        ),
        migrations.AddField(
            model_name='eleve',
            name='clee_prive_serveur',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='eleve',
            name='clee_publique_client',
            field=models.IntegerField(default=0),
        ),
    ]
