# Generated by Django 4.0.6 on 2022-08-12 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_alter_ageinganalysismodel_totqua'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ageinganalysismodel',
            name='Values',
        ),
        migrations.AlterField(
            model_name='ageinganalysismodel',
            name='totqua',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
