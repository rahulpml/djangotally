# Generated by Django 4.0.6 on 2022-08-12 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_ageinganalysismodel_value_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ageinganalysismodel',
            name='value',
            field=models.IntegerField(default=0),
        ),
    ]
