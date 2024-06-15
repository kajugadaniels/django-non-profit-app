from django.contrib import admin
from sponsor.models import *

class FavoriteStudentAdmin(admin.ModelAdmin):
    list_display = ('sponsor', 'student')
    search_fields = ('sponsor__email', 'student__name')

admin.site.register(Letter)
admin.site.register(SponsorDonateStudent)
admin.site.register(FavoriteStudent, FavoriteStudentAdmin)
admin.site.register(DonorToStudent)