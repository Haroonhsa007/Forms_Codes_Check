# Generated by Django 3.2.5 on 2022-05-02 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('harvest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]