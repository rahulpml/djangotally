from ast import alias
from django.db import models

# Create your models here.

#stockgroupModel
class StockGroupModel(models.Model):
    group_name = models.CharField(max_length=225, null=False, blank=False)
  

    def __str__(self):
        return self.group_name

#createstockGroupModel

class MainStockGroupModel(models.Model):
    gname=models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    under= models.CharField(max_length=225 ,unique=True ,null =True)
    quantities=models.CharField(max_length=225,null=True)
    gst = models.CharField(max_length=225,null=True)
    group = models.ForeignKey(StockGroupModel,on_delete=models.SET_NULL, null=True)
    

    def __str__(self):
        return self.gname

#stockcat
class StockCategoryModel(models.Model):
    cat_name = models.CharField(max_length=225, null=False, blank=False)
   

    def __str__(self):
        return self.cat_name

#mainstockCategory  models.

class MainStockCategoryModel(models.Model):
    cname=models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    under= models.CharField(max_length=225 ,null=True ,unique=True)
    quantities=models.CharField(max_length=100,null=True)
    category = models.ForeignKey(StockCategoryModel,on_delete=models.SET_NULL, null=True)
    
     

    def __str__(self):
        return self.cname









