from django.shortcuts import render

# Create your views here.
def Mycalc(request):
    return render (request,'calcul.html')