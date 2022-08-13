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
    under= models.ForeignKey(StockGroupModel,on_delete=models.SET_NULL, null=True)
    quantities=models.CharField(max_length=225,null=True)

    def __str__(self):
        return self.gname



class AgeingAnalysisModel(models.Model):
    pname = models.ForeignKey(MainStockGroupModel ,on_delete = models.SET_NULL,null=True)
    expdate = models.DateField(null=True)
    totqua = models.IntegerField(default=0, null=True,)
    value = models.IntegerField(default=0 ,null=True)
    def __str__(self):
        return self.pname

