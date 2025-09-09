from django.shortcuts import render

def show_main(request):
    context = {
        'app_name' : 'Monokotil-Shop',
        'name': 'Rafsanjani',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
# Create your views here.
