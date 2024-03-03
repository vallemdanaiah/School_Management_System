from django.shortcuts import render,redirect
from .models import TecDetailes
from django.contrib import messages
# Create your views here

def Teacherlogin(request):
    if request.method == 'POST':
        Tecname = request.POST.get('Tecname') 
        print('tecname',Tecname)       
        Tecpassword = request.POST.get('Tecpassword') 
        print('tecpassword',Tecpassword)       
        print('Tecname=',Tecname,'Tecpassword=',Tecpassword)  # Debugging print statement
        try:
            check = TecDetailes.objects.get(Tecname=Tecname, Tecpassword=Tecpassword)
            print('check',check)
            return render(request, 'teacher/teacherhome.html', {})
        except TecDetailes.DoesNotExist:            
            messages.error(request, 'Invalid name and email')
    return render(request, 'teacherlogin.html', {})

def Teacherlist(request):
    data = TecDetailes.objects.all()
    return render(request,'teacher/teacherlist.html',{'data':data})

# Delete View
def delete(request,id):
    a=TecDetailes.objects.get(pk=id)
    a.delete()
    return redirect('Teacherlist')  
    
#update View
# def Update_record(request,id):
#     if request.method=='POST':
#         data=TecDetailes.objects.get(pk=id)
#         form=TecDetailesForm(request.POST,instance=data)
#         if form.is_valid():
#            form.save()
#         return redirect('studentregisteractions')
#     else:
#         data=TecDetailes.objects.get(pk=id)
#         form=TecDetailesForm(instance=data)
#     context={'form':form,'data':data}
#     return render (request,'student/update.html',context)
    
