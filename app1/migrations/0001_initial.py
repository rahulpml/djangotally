# Generated by Django 4.0.6 on 2022-08-12 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgeingAnalysisModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=225)),
                ('expdate', models.DateField(null=True)),
                ('totqua', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
