# Generated by Django 5.0.3 on 2024-03-25 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='s',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuno', models.CharField(max_length=10)),
                ('stuname', models.CharField(max_length=10)),
                ('stuclass', models.CharField(max_length=10)),
                ('stuage', models.CharField(max_length=10)),
                ('stusex', models.CharField(max_length=10)),
                ('stuphone', models.CharField(max_length=20)),
                ('stuaddress', models.CharField(max_length=10)),
            ],
        ),
    ]