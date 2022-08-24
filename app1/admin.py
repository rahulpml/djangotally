from django.contrib import admin

from .models import CreateStockGroupModel , CreateStockcategoryModel,MainStockCategoryModel,MainStockGroupModel

# Register your models here.
admin.site.register(CreateStockcategoryModel)
admin.site.register(CreateStockGroupModel)
admin.site.register(MainStockCategoryModel)
admin.site.register(MainStockGroupModel)