# Generated by Django 4.1 on 2022-08-30 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0026_remove_mainstockcategorymodel_created_on_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainstockgroupmodel',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]