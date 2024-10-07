from django.shortcuts import render

# Create your views here.

def square_view(request):
    return render(request, 'square.html')