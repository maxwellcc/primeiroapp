# Generated by Django 3.1.7 on 2021-03-09 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BancoProblema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=30)),
                ('problema', models.CharField(max_length=250)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=2)),
            ],
        ),
    ]