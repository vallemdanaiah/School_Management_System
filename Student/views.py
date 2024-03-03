from django.shortcuts import render,redirect
# Create your views here.
from .forms import RegisterModelForm
from .models import RegisterModel
from django.contrib import messages

def studentregisteractions(request):
    if request.method == 'POST':
        form = RegisterModelForm(request.POST)
        if form.is_valid():  
            form.save()        
            messages.success(request, 'You have been successfully registered')            
            form = RegisterModelForm()
            return render(request,'student/register.html',{'form':form})
        else:
            messages.success(request, 'Email or Mobile Already Existed')
            print("Invalid form")
    else:
        form = RegisterModelForm()
    return render(request,'student/register.html',{'form':form})
    
def userlogin(request):
    if request.method == 'POST':
        studentname = request.POST.get('studentname')        
        studentpassword = request.POST.get('studentpassword')        
        print('studentname=', studentname, 'studentpassword=', studentpassword)  # Debugging print statement
        try:
            check = RegisterModel.objects.filter(studentname=studentname, studentpassword=studentpassword)
            return render(request, 'student/studenthome.html', {})
        except RegisterModel.DoesNotExist:            
            messages.error(request, 'Invalid name and email')
    return render(request, 'studentlogin.html', {})

def userlist(request):
    data = RegisterModel.objects.all()
    return render(request,'student/studentlist.html',{'data':data})

# Delete View
def Delete_record(request,id):
    a=RegisterModel.objects.get(pk=id)
    a.delete()
    return redirect('userlist')  
    
#update View
def Update_record(request,id):
    if request.method=='POST':
        data=RegisterModel.objects.get(pk=id)
        form=RegisterModelForm(request.POST,instance=data)
        if form.is_valid():
           form.save()
        return redirect('studentregisteractions')
    else:
        data=RegisterModel.objects.get(pk=id)
        form=RegisterModelForm(instance=data)
    context={'form':form,'data':data}
    return render (request,'student/update.html',context)
    



    
    



