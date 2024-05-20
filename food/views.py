from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader
# Create your views here.
def index(request):
    list_item=Item.objects.all()
    template=loader.get_template('food/index.html')
    context={
        'list_item':list_item,
        
    }
    return HttpResponse(template.render(context,request))
def items(request):
    return HttpResponse('<h1>this is item view</h1>')
def details(request,item_id):
    item=Item.objects.get(pk=item_id)
    context={
        'item':item,
    }
    return render(request,'food/detail.html',context)