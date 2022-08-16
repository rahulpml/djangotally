from django.contrib import admin

from .models import StockGroupModel ,MainStockGroupModel , StockCategoryModel , MainStockCategoryModel

# Register your models here.
admin.site.register(StockGroupModel)
admin.site.register(MainStockGroupModel)
admin.site.register(StockCategoryModel)
admin.site.register(MainStockCategoryModel)
