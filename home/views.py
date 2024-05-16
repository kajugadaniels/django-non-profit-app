from django.shortcuts import render

def index(request):
    return render(request, 'frontend/index.html')

def history(request):
    return render(request, 'frontend/history.html')

def whatWeDo(request):
    return render(request, 'frontend/what-we-do/index.html')

def students(request):
    return render(request, 'frontend/students/index.html')