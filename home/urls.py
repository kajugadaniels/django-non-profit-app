from django.urls import path
from django.conf import settings
from .views import *
from django.conf.urls.static import static
from django.contrib import admin

app_name = 'frontend'

urlpatterns = [
   path('login/', user_login, name="login"),
   path('register/', user_register, name="register"),

   path('dashboard', dashboard, name="dashboard"),

   path('', index, name="home"),

   path('about-rwanda/', aboutRwanda, name="aboutRwanda"),
   path('our-history/', history, name="history"),
   path('mission-vision-values/', missionVisionValues, name="missionVisionValues"),

   path('team/', team, name="team"),
   path('team/<slug>', teamMember, name="teamMember"),

   path('what-we-do/', whatWeDo, name="whatWeDo"),
   path('what-we-do/education', education, name="education"),
   path('what-we-do/vocational-training', vocationalTraining, name="vocationalTraining"),
   path('what-we-do/medical-care-outreach', medicalCare, name="medicalCare"),
   path('what-we-do/community-empowerment', communityEmpowerment, name="communityEmpowerment"),
   path('what-we-do/tunga-women-initiative', tungaWomen, name="tungaWomen"),
   path('what-we-do/story/<slug>', story, name="story"),

   path('students/', students, name="students"),
   path('student/<slug:slug>/', getStudent, name='getStudent'),

   path('give/', give, name="give"),
   path('donate/', donate, name="donate"),
   path('store/', store, name="store"),
   path('store/<slug>', product, name="product"),
   
   path('monthly-donating/', monthlyDonating, name="monthlyDonating"),
   
   path('blog/', blog, name="blog"),
   path('blog/<slug>', viewBlog, name="viewBlog"),
   
   path('projects/', projects, name="projects"),
   path('project/<slug>', viewProject, name="viewProject"),
   
   path('faq/', faq, name="faq"),

   path('pray-with-us/', prayWithUs, name="prayWithUs"),

   path('contact/', contact, name="contact"),

   path('checkout/', checkout, name="checkout"),
   path('give-gift/', checkoutpay, name="givegift"),
   path('remove_from_cart/', remove_from_cart, name='remove_from_cart'),

   path('get-involved', getInvolved, name="getInvolved"),
   path('visit-us', visitUs, name="visitUs"),
   path('volunteers', volunteers, name="volunteers"),
   
   path('campaigns', campaigns, name="campaigns"),
   path('campaigns/<slug>', viewCampaign, name="viewCampaign"),

   path('terms-and-conditions', termsAndConditions, name="termsAndConditions"),
   path('privacy-policy', privacyPolicy, name="privacyPolicy"),
   path('child-protection-policy', childProtectionPolicy, name="childProtectionPolicy"),

   path('resources', resources, name="resources"),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'AOF Administration'                  
admin.site.index_title = 'Dashboard'                
admin.site.site_title = 'AOF Admin'