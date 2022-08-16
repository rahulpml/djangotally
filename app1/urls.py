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

    path('maingroupsview',views.maingroupsview,name='maingroupsview'),
    path('maincategoryview',views.maincategoryview,name='maincategoryview'),
    path('categorysallview',views.categorysallview,name='categorysallview'),
    path('creategroupsview',views.creategroupsview,name='creategroupsview'),
    path('createcategoryview',views.createcategoryview,name='createcategoryview'),
    path('savestockgroup',views.savestockgroup,name='savestockgroup'),
  
    





    
]
 