from django.shortcuts import render

# Create your views here.
def corporate(request):
    return render(request, './corporate/corporate.html')