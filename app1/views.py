from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import redirect

from app1.models import CreateStockGroupModel , CreateStockcategoryModel,MainStockCategoryModel,MainStockGroupModel

# Create your views here.

def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'home.html')

def group(request):
    return render(request, 'groups.html')

def branch(request):
    return render(request, 'branch.html')

def ledger(request):
    return render(request, 'ledger.html')

def primary(request):
    return render(request, 'primarycost.html')

def costcat(request):
    return render(request, 'costcat.html')

def costcentr(request):
    return render(request, 'costcentr.html')

def voucher(request):
    return render(request, 'voucher.html')

def vouchpage(request):
    return render(request, 'vouchpage.html')

#creategroupsview your

def maingroupsview(request):
    groups=MainStockGroupModel.objects.all()
    context={
        'groups':groups,
        } 
    return render(request,'maingroups.html',context)

#createmaingroups
def maincategoryview(request):
    category=MainStockCategoryModel.objects.all()
    context={
        'category':category,
        } 
    return render(request,'maincategory.html',context)

#createcategoryview
def categorysummary(request):
    groups=MainStockGroupModel.objects.all()
    context={
        'groups':groups,
        } 
    return render(request,'groupsummary.html',context)


#creategroupsview

def creategroupsview(request):
    groups=CreateStockGroupModel.objects.all()
    context={
        'groups':groups,
        } 
    return render(request, 'creategroups.html',context)    

#createcategoryview
def createcategoryview(request):
    category=CreateStockcategoryModel.objects.all()
    context={
        'category':category,
        } 
    return render(request, 'createcategory.html',context) 

#savestockgroupview 

def savestockgroupview(request):
    if request.method=='POST':
        gpname=request.POST['name']
        s=CreateStockGroupModel(grp_name=gpname)
        s.save()
        abr=request.POST['alias']
        grp=request.POST.get('u')
        gp=CreateStockGroupModel.objects.get(grp_name=grp)
        q=request.POST.get('qty')
        gst=request.POST.get('gst')
        sg=MainStockGroupModel(name=gpname,alias=abr,quantities=q,under=grp,group=gp, gst=gst)
        sg.save()
        return redirect('maingroupsview')
        
#svaestocksgroup
def savestockcategoryview(request):
    if request.method=='POST':
        catname=request.POST['name']
        s=CreateStockcategoryModel(cat_name=catname)
        s.save()
        abr=request.POST['alias']
        cat=request.POST.get('u')
        c=CreateStockcategoryModel.objects.get(cat_name=cat)
        q=request.POST.get('qty')
        sc=MainStockCategoryModel(name=catname,alias=abr,quantities=q,under=cat,category=c)
        sc.save()
        return redirect('maincategoryview')

#createstockageingviewview

def stockageingsview(request):
    return render(request, 'stockageings.html')



def stockitemmonthlysummaryview(request):
    return render(request, 'stockitemmonthlysummary.html')



def stockitemvouchersview(request):
    return render(request, 'stockitemvouchers.html')

def costestimateview(request):
    return render(request, 'costestimate.html')


