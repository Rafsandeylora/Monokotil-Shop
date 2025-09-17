from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProducForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
def show_main(request):
    products_list = Product.objects.all()
    context = {
        'app_name' : 'Monokotil-Shop',
        'name': 'Rafsanjani',
        'class': 'PBP A',
        'products_list': products_list,
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProducForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_product(request, id):
    products = get_object_or_404(Product, pk=id)

    context = {
        'product': products
    }
    return render(request, "product_details.html", context)

def show_xml(request):
     news_list = Product.objects.all()
     xml_data = serializers.serialize("xml", news_list)
     return HttpResponse(xml_data, content_type="application/xml")
 
def show_json(request):
    news_list = Product.objects.all()
    json_data = serializers.serialize("json", news_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, news_id):
   try:
       news_item = Product.objects.filter(pk=news_id)
       xml_data = serializers.serialize("xml", news_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, news_id):
   try:
       news_item = Product.objects.get(pk=news_id)
       json_data = serializers.serialize("json", [news_item])
       return HttpResponse(json_data, content_type="application/json")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

