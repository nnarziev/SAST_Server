# Generated by Django 2.2 on 2019-04-27 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('username', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=16)),
            ],
        ),
    ]