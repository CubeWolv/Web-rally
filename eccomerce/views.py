from django.shortcuts import render

# Create your views here.
def eccomerce(request):
    return render(request, './eccomerce/eccomerce.html')