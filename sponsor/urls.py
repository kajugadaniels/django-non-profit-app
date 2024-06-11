from django.urls import path
from django.conf import settings
from sponsor.views import *
from django.conf.urls.static import static
from django.contrib import admin

app_name = 'sponsor'

urlpatterns = [
    path('login/', user_login, name="login"),
    path('register/', user_register, name="register"),
    path('logout/', logout_user, name='logout'),

    path('dashboard/', dashboard, name="dashboard"),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'AOF Administration'                  
admin.site.index_title = 'Dashboard'                
admin.site.site_title = 'AOF Admin'