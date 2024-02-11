from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def home(request):
    return render(request,"home.html")
@csrf_exempt
def logout_view(request):
    logout(request)
    return redirect("/")
