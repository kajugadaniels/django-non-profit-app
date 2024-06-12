from django.contrib import admin
from .forms import CustomUserCreationForm,CustomUserChangeForm
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = UserAccount
    list_display = ("email","is_staff", "is_active",'firstname', 'lastname',"phonenumber","user_type")
    list_filter = ("email", "is_staff", "is_active",'firstname')
    fieldsets = (
        (None, {"fields": ("email","password","user_type","phonenumber")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff","firstname", "lastname",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)

admin.site.register(UserAccount, CustomUserAdmin)
admin.site.register(Donate)
admin.site.register(StudentDonations)
admin.site.register(Donation)
admin.site.register(DonateGifts)
# admin.site.register(DonateToBeneficiary)
