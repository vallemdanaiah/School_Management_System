from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request,'index.html',{})

def studentlogin(request):
    return render(request,'studentlogin.html',{})

def teacherlogin(request):
    return render(request,'teacherlogin.html',{})

def logout(request):
    return render(request,'index.html')
