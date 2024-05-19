from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
import string, random
from django.utils.text import slugify
from backend.models import *
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
    phonenumber = models.CharField(_("phonenumber"), max_length=255,null=True,blank=True)
    user_type = models.CharField(max_length=255,choices=choices, null=True,blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Donate(models.Model):
    donationTitle= models.CharField(max_length=255)
    amount = models.FloatField()
    donationId = models.TextField(max_length=255)
    productId = models.TextField(max_length=255)
    created_on =  models.DateTimeField(default=timezone.now)
    paymentMode = models.TextField(max_length=255)
    donatedby = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    status =models.CharField(max_length=255, default="Pending")
    slug = models.SlugField(unique=True, max_length=150, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.donationTitle)
            random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
            self.slug = f"{base_slug}-{random_string}"
        super().save(*args, **kwargs)
    def __str__(self) -> str:
        return self.donationTitle
    

class DonateToStudents(models.Model):
    donationTitle= models.CharField(max_length=255)
    donationId = models.TextField(max_length=255)
    productId = models.TextField(max_length=255)
    created_on =  models.DateTimeField(default=timezone.now)
    beneficiary = models.ForeignKey(Student, on_delete=models.CASCADE)
    paymentMode = models.TextField(max_length=255)
    donatedBy = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    slug = models.SlugField(unique=True, max_length=150, blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.donationTitle)
            random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
            self.slug = f"{base_slug}-{random_string}"
        super().save(*args, **kwargs)
    def __str__(self) -> str:
        return self.donationTitle