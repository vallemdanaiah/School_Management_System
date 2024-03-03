"""School URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from School import views as mainview
from Student import views as stdview
from Teacher import views as tecview
from HM import views as hmview
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainview.base, name='base'),
    path('studentlogin',mainview.studentlogin, name='studentlogin'),
    path('teacherlogin', mainview.teacherlogin, name='teacherlogin'),
    path('logout',mainview.logout, name='logout'),  
    #student urls
    path('studentregisteractions', stdview.studentregisteractions, name='studentregisteractions'),
    path('userlogin', stdview.userlogin ,name='userlogin' ),
    path('userlist', stdview.userlist, name='userlist'),
    path('Delete_record/<int:id>', stdview.Delete_record,name='Delete_record'),
    path('Update_record<int:id>', stdview.Update_record,name='Update_record'),
    
    #teacher urls
    path('Teacherlogin', tecview.Teacherlogin, name='Teacherlogin'),
    path('Teacherlist', tecview.Teacherlist, name='Teacherlist'),
    path('delete/<int:id>/', tecview.delete, name='delete'),
    
    #hmviews
    path('HMlogin',hmview.HMlogin, name='HMlogin'),
    path('teachers',hmview.teachers, name='teachers'),
    path('students',hmview.students, name='students')
    ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

