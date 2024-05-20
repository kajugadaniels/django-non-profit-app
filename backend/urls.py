from django.urls import path
from django.conf import settings
from backend.views import *
from django.conf.urls.static import static
from django.contrib import admin

app_name = 'backend'

urlpatterns = [
   path('login/', user_login, name="login"),
   path('logout/', user_logout, name='logout'),

   path('dashboard/', dashboard, name="dashboard"),

   path('students/', getStudents, name='getStudents'),
   path('student/create', addStudent, name='addStudent'),
   path('student/<slug>', editStudent, name='editStudent'),

   path('team/', getTeam, name='getTeam'),
   path('team/create', addTeam, name='addTeam'),
   path('team/<slug>', editTeam, name='editTeam'),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'AOF Administration'                  
admin.site.index_title = 'Dashboard'                
admin.site.site_title = 'AOF Admin'