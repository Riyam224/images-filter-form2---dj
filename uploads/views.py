from django.shortcuts import redirect, render

# Create your views here.
from .models import Product
from .forms import ProductForm

def index(request):
    products = Product.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    form = ProductForm()

    return render(request , 'index.html', {
        'products': products ,
        'form': form
    })