# Generated by Django 4.0.6 on 2022-08-12 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_alter_ageinganalysismodel_pname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ageinganalysismodel',
            name='value',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
