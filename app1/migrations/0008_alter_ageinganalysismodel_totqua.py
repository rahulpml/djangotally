# Generated by Django 4.0.6 on 2022-08-12 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_rename_value_ageinganalysismodel_values'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ageinganalysismodel',
            name='totqua',
            field=models.IntegerField(default=0),
        ),
    ]