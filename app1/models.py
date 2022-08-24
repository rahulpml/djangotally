from ast import alias
from django.db import models

# Create your models here.

class CreateStockGroupModel(models.Model):
    grp_name = models.CharField(max_length=70, null=False, blank=False)

    def __str__(self):
        return self.grp_name
class CreateStockcategoryModel(models.Model):
    cat_name = models.CharField(max_length=70, null=False, blank=False)

    def __str__(self):
        return self.cat_name

class MainStockGroupModel(models.Model):
    name=models.CharField(max_length=100)
    alias=models.CharField(max_length=100)
    under=models.CharField(max_length=100,null=True)
    quantities=models.CharField(max_length=100,null=True)
    gst = models.CharField(max_length=100,null=True)
    group = models.ForeignKey(CreateStockGroupModel,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
    
class MainStockCategoryModel(models.Model):
    name=models.CharField(max_length=100)
    alias=models.CharField(max_length=100)
    under=models.CharField(max_length=50)
    quantities=models.CharField(max_length=100,null=True)
    category = models.ForeignKey(CreateStockcategoryModel,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name






