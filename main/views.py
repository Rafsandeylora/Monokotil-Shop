from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406495400',
        'name': 'Rafsanjani',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
# Create your views here.
