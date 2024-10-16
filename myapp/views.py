from django.shortcuts import render, redirect, get_object_or_404
from .forms import ItemCreateForm
from .models import MyItem

def item_create(request):
    if request.method == 'POST':
        form = ItemCreateForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('item_list')  # Redirect to the item list page
    else:
        form = ItemCreateForm()
    return render(request, 'myapp/item_form.html', {'form': form})

def item_list(request):
    items = MyItem.objects.all()  # Get all items
    return render(request, 'myapp/item_list.html', {'items': items})

def item_delete(request, item_id):
    item = get_object_or_404(MyItem, id=item_id)  # Get the item or 404
    if request.method == 'POST':
        item.delete()  # Delete the item
        return redirect('item_list')  # Redirect to the item list page
    return render(request, 'myapp/item_confirm_delete.html', {'item': item})
