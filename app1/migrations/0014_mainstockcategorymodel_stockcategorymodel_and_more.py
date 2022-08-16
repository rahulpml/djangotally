# Generated by Django 4.0.6 on 2022-08-15 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_alter_ageinganalysismodel_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainStockCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=225)),
                ('alias', models.CharField(max_length=225)),
                ('quantities', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='StockCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=225)),
            ],
        ),
        migrations.AddField(
            model_name='mainstockgroupmodel',
            name='gst',
            field=models.CharField(max_length=225, null=True),
        ),
        migrations.DeleteModel(
            name='AgeingAnalysisModel',
        ),
        migrations.AddField(
            model_name='mainstockcategorymodel',
            name='under',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.stockcategorymodel'),
        ),
    ]