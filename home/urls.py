from django.urls import path
from django.conf import settings
from .views import *
from django.conf.urls.static import static
from django.contrib import admin

app_name = 'frontend'

urlpatterns = [
   path('', index, name="home"),
   path('our-history/', history, name="history"),
   path('what-we-do/', whatWeDo, name="whatWeDo"),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'AOF Administration'                  
admin.site.index_title = 'Dashboard'                
admin.site.site_title = 'AOF Admin'