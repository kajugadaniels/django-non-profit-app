from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
# Create your models here.
class UserAccount(AbstractBaseUser, PermissionsMixin):
    ADMIN = 'admin'
    USER = 'user'
    choices =[
        (USER,'users'),
        (ADMIN,'admin'),
    ]
    email = models.EmailField(_("email address"), unique=True)
    firstname = models.CharField(_("First name"), max_length=255)
    lastname = models.CharField(_("Last name"), max_length=255)
    phonenumber = models.CharField(_("Phonenumber"), max_length=255,null=True,blank=True)
    user_type = models.CharField(max_length=255,choices=choices, null=True,blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email