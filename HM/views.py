from django.shortcuts import render
from django.contrib import messages
from Teacher.models import TecDetailes
from Student.models import RegisterModel
# Create your views here.
def HMlogin(request):
    if request.method == 'POST':
        usrid = request.POST.get('usrid')
        pswd = request.POST.get('pswd')
        print("User ID is = ", usrid)
        if usrid == 'admin' and pswd == 'admin':
            return render(request, 'hm/hmhome.html')

        else:
            messages.success(request, 'Please Check Your Login Details')
    return render(request, 'hmlogin.html', {})

def teachers(request):
    data = TecDetailes.objects.all()
    return render(request,'hm/list.html',{'data':data})

def students(request):
    data = RegisterModel.objects.all()
    return render(request,'hm/list1.html',{'data':data}) 
