# Generated by Django 4.0.6 on 2022-08-16 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0019_alter_mainstockcategorymodel_under'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainstockcategorymodel',
            name='quantities',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
