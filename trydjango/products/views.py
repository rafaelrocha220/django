from queue import Empty
from django.shortcuts import render
from .forms import ProductForm

# Create your views here.
def view_create(req):
    form = ProductForm(req.POST or None)
    if(form.is_valid()):
        form.save()
    
    context = {
        'form': form
    }
    
    return render(req, 'products/create.html', context)