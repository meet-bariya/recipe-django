from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm

# Create your views here.
def index(request):
    return HttpResponse('Hello World!')

def items(request):
    item_list = Item.objects.all()
    return render(request, 'food/items.html', context={'item_list':item_list})

def item_detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    return render(request, 'food/item-detail.html', context={'item':item})

def item_add(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:items')
    return render(request, 'food/item-form.html', context={'form':form})

def item_delete(request, item_id):
    item = Item.objects.get(pk=item_id)
    item.delete()
    return redirect('food:items')