from django.shortcuts import render
from .models import ItemList
from django.http import HttpResponseRedirect 

# Create your views here.
def index(request):
    return render (request, 'index.html')


def ViewRecipies(request):
    items = ItemList.objects.all()
    return render(request, 'List.html',  {'all_items':items})

def AdminRecipies(request):
    items = ItemList.objects.all()
    return render(request, 'Add.html', {'all_items':items})

def addrecipies(request):
    new_item = ItemList()
    new_item.recipie = request.POST.get('recipie')
    new_item.save()
    return HttpResponseRedirect('/radmin/') 



