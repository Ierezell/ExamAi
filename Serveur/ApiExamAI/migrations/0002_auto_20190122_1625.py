# Generated by Django 2.1.5 on 2019-01-22 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiExamAI', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eleve',
            name='secretPartage',
        ),
        migrations.AlterField(
            model_name='eleve',
            name='dateCo',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date de connection'),
        ),
        migrations.AlterField(
            model_name='eleve',
            name='photo',
            field=models.ImageField(default=None, null=True, upload_to='static/images/eleves/'),
        ),
        migrations.AlterField(
            model_name='eleve',
            name='suspect',
            field=models.IntegerField(default=0),
        ),
    ]
