# Generated by Django 5.0.3 on 2024-04-13 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_stus3_cards'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scores',
            name='grade',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='scores',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
