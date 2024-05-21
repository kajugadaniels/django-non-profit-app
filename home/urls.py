from django.urls import path
from django.conf import settings
from .views import *
from django.conf.urls.static import static
from django.contrib import admin

app_name = 'frontend'

urlpatterns = [
   path('', index, name="home"),

   path('our-history/', history, name="history"),
   path('team/', team, name="team"),

   path('what-we-do/', whatWeDo, name="whatWeDo"),
   path('what-we-do/education', education, name="education"),
   path('what-we-do/farming-outreach', farmingOutreach, name="farmingOutreach"),
   path('what-we-do/feeding-outreach', feedingOutreach, name="feedingOutreach"),
   path('what-we-do/education-sponsorship-program', educationSponsorship, name="educationSponsorship"),
   path('what-we-do/medical-care-outreach', medicalCare, name="medicalCare"),
   path('what-we-do/Oasis-christian-academy', OasisAcademy, name="OasisAcademy"),
   path('what-we-do/gospel-teaching', gospelTeaching, name="gospelTeaching"),

   path('students/', students, name="students"),
   path('student/<slug>', getStudent, name='getStudent'),

   path('give/', give, name="give"),
   path('donate/', donate, name="donate"),
   path('store/', store, name="store"),
   path('store/<slug>', product, name="product"),
   
   path('blog/', blog, name="blog"),
   path('blog/<slug>', viewBlog, name="viewBlog"),
   
   path('projects/', projects, name="projects"),
   path('project/<slug>', viewProject, name="viewProject"),
   
   path('faq/', faq, name="faq"),

   path('contact/', contact, name="contact"),
   
   path('terms-and-conditions', termsAndConditions, name="termsAndConditions")
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'AOF Administration'                  
admin.site.index_title = 'Dashboard'                
admin.site.site_title = 'AOF Admin'