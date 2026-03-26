from django.shortcuts import render

def homepage(request):
    return render(request, 'frontend/homepage.html')

def fanpage(request):
    return render(request, 'frontend/fanpage.html')

def chat(request):
    return render(request, 'frontend/chat.html')