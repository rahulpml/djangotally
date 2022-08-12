from django.shortcuts import render

from .models import MainStockGroupModel, StockGroupModel

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


#listingStockgroups

def listofstockgroups(request):
    grps = StockGroupModel.objects.all()
    context ={
        'grps':grps
    }
    return render(request,'listofstockgroups.html' , context)

#creating MainstockGroup

def mainstockgroups(request):
    grps= MainStockGroupModel.objects.all()
    context={
        'grps':grps,
        } 
    return render(request,'stockgroups.html',context)






def costcataug15(request):
    return render(request, 'costcat.html')