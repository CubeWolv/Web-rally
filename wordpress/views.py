from django.shortcuts import render

# Create your views here.
def wordpress(request):
    return render(request, './wordpress/wordpress.html')