from django.urls import path,include
from.import views


urlpatterns = [

    path('',views.base,name='base'),
    path('index',views.index,name='index'),
    path('group',views.group,name='group'),
    path('branch',views.branch,name='branch'),
    path('ledger',views.ledger,name='ledger'),
    path('primary',views.primary,name='primary'),
    path('costcat',views.costcat,name='costcat'),
    path('costcentr',views.costcentr,name='costcentr'),
    path('voucher',views.voucher,name='voucher'),
    path('vouchpage',views.vouchpage,name='vouchpage'),

    path('maincategoryview',views.maincategoryview,name='maincategoryview'),
    path('maingroupsview',views.maingroupsview,name='maingroupsview'),
    path('creategroupsview',views.creategroupsview,name='creategroupsview'),
    path('categorysummary',views.categorysummary,name='categorysummary'),
    path('createcategoryview',views.createcategoryview,name='createcategoryview'),
    path('savestockgroupview',views.savestockgroupview,name='savestockgroupview'),
    path('savestockcategoryview',views.savestockcategoryview,name='savestockcategoryview'),
    path('stockageingsview',views.stockageingsview,name='stockageingsview'),
    path('stockitemmonthlysummaryview',views.stockitemmonthlysummaryview,name='stockitemmonthlysummaryview'),
    path('stockitemvouchersview',views.stockitemvouchersview,name='stockitemvouchersview'),
    path('costestimateview',views.costestimateview,name='costestimateview'),

  

    
]
 