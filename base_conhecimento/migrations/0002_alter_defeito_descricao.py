# Generated by Django 5.2 on 2025-04-05 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_conhecimento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defeito',
            name='descricao',
            field=models.TextField(max_length=250),
        ),
    ]
