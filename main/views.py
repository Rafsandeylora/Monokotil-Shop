from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProducForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import datetime
from django.views.decorators.csrf import csrf_exempt

# --- Authentication Views ---
def register(request):
    form = UserCreationForm()
    # Logika ini untuk penanganan non-AJAX jika diperlukan
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun berhasil dibuat!')
            return redirect('main:login')
    context = {'form': form}
    return render(request, 'register.html', context)

@csrf_exempt
def register_ajax(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"status": "success", "message": "Akun berhasil dibuat!"}, status=201)
        else:
            # Mengirimkan detail error untuk ditampilkan di frontend
            return JsonResponse({"status": "error", "errors": form.errors}, status=400)
    return JsonResponse({"status": "error", "message": "Metode tidak valid."}, status=405)

def login_user(request):
    # Logika ini untuk penanganan non-AJAX jika diperlukan
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

@csrf_exempt
def login_ajax(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                response_data = {"status": "success", "message": "Login berhasil!"}
                response = JsonResponse(response_data)
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
        return JsonResponse({"status": "error", "message": "Username atau password salah."}, status=401)
    return JsonResponse({"status": "error", "message": "Metode tidak valid."}, status=405)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

# --- Main Page and Product Views ---
@login_required(login_url='/login')
def show_main(request):
    form = ProducForm()
    context = {
        'form': form,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "main.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {
        'product': product
    }
    return render(request, "product_details.html", context)

# --- AJAX Views for Products ---
@login_required
def get_product_json(request):
    filter_param = request.GET.get('filter')
    if filter_param == 'my_products':
        # Hanya tampilkan produk milik user yang sedang login
        products = Product.objects.filter(user=request.user)
    else:
        # Tampilkan semua produk
        products = Product.objects.all()
    return HttpResponse(serializers.serialize('json', products))

@csrf_exempt
@login_required
def create_product_ajax(request):
    if request.method == 'POST':
        form = ProducForm(request.POST)
        
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return JsonResponse({"status": "success", "message": "Produk berhasil ditambahkan!"}, status=201)
        else:
            return JsonResponse({"status": "error", "errors": form.errors}, status=400)
    return JsonResponse({"status": "error", "message": "Metode tidak valid."}, status=405)

@csrf_exempt
@login_required
def delete_product_ajax(request, id):
    if request.method == 'POST':
        try:
            # Pastikan hanya pemilik produk yang bisa menghapus
            product = get_object_or_404(Product, pk=id, user=request.user)
            product.delete()
            return JsonResponse({"status": "success", "message": "Produk berhasil dihapus."}, status=200)
        except Product.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Produk tidak ditemukan atau Anda tidak punya izin."}, status=404)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
    return JsonResponse({"status": "error", "message": "Metode tidak valid."}, status=405)

@csrf_exempt
@login_required
def edit_product_ajax(request, id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=id, user=request.user)
        form = ProducForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return JsonResponse({"status": "success", "message": "Produk berhasil diupdate!"}, status=200)
        else:
            return JsonResponse({"status": "error", "errors": form.errors}, status=400)
    return JsonResponse({"status": "error", "message": "Metode tidak valid."}, status=405)

def show_xml(request):
     product_list = Product.objects.all()
     return HttpResponse(serializers.serialize("xml", product_list), content_type="application/xml")
 
def show_json(request):
    product_list = Product.objects.all()
    return HttpResponse(serializers.serialize("json", product_list), content_type="application/json")

def show_xml_by_id(request, product_id):
   product_item = Product.objects.filter(pk=product_id)
   return HttpResponse(serializers.serialize("xml", product_item), content_type="application/xml")

def show_json_by_id(request, product_id):
   product_item = Product.objects.filter(pk=product_id)
   return HttpResponse(serializers.serialize("json", product_item), content_type="application/json")