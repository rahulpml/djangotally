from django.contrib import admin

from .models import AgeingAnalysisModel ,StockGroupModel ,MainStockGroupModel

# Register your models here.
admin.site.register(StockGroupModel)
admin.site.register(MainStockGroupModel)
admin.site.register(AgeingAnalysisModel)
