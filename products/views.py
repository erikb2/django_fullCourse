from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Product
from .forms import ProductForm

# Vista antes de utilizar Vistas Basadas en Clases
'''
def hello_world(request):
	product  = Product.objects.order_by('id')
	template = loader.get_template('index.html')
	context  = {
		'product': product
	}
	return HttpResponse(template.render(context, request))
'''

def product_detail(request, pk):
	product = get_object_or_404(Product, pk = pk)
	template = loader.get_template('product_detail.html')
	context = {
		'product': product
	}
	return HttpResponse(template.render(context, request))

def new_product(request):
	if request.method == 'POST':
		form     = ProductForm(request.POST, request.FILES) # request.FILES let the POST of files.
		if form.is_valid():
			product = form.save(commit=False)
			product.save()
			return HttpResponseRedirect('/')
	else:
		form = ProductForm()
	
	template = loader.get_template('new_product.html')
	context  = {
		'form': form
	}
	return HttpResponse(template.render(context, request))


class ProductList(ListView):
	model = Product

class ProductDetail(DetailView):
	model = Product