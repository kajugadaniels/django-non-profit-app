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
   path('student/<slug>/delete/', deleteStudent, name='deleteStudent'),

   path('team/', getTeam, name='getTeam'),
   path('team/create', addTeam, name='addTeam'),
   path('team/<slug>', editTeam, name='editTeam'),
   path('team/<slug>/delete/', deleteTeam, name='deleteTeam'),

   path('store/', getProduct, name='getProduct'),
   path('store/create', addProduct, name='addProduct'),
   path('store/<slug>', editProduct, name='editProduct'),
   path('product/<slug>/delete/', deleteProduct, name='deleteProduct'),

   path('projects/', getProjects, name='getProjects'),
   path('project/create', addProject, name='addProject'),
   path('project/<slug>', editProject, name='editProject'),
   path('project/<slug>/delete/', deleteProject, name='deleteProject'),

   path('blog/', getBlog, name='getBlog'),
   path('blog/create', addBlog, name='addBlog'),
   path('blog/<slug>', editBlog, name='editBlog'),
   path('blog/<slug>/delete/', deleteBlog, name='deleteBlog'),

   path('donate/', donate, name='donate'),
   path('donate-to-student', donateToStudent, name='donateToStudent'),

   path('settings/', setting, name='settings')
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'AOF Administration'                  
admin.site.index_title = 'Dashboard'                
admin.site.site_title = 'AOF Admin'