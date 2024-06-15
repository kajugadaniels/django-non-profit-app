from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
import string, random
from django.utils.text import slugify
from backend.models import *

class UserAccount(AbstractBaseUser, PermissionsMixin):
    ADMIN = 'admin'
    USER =  'user'
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
        return self.email

class Donation(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    project = models.ForeignKey(ProjectDetails, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class DonateGifts(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255, blank=True, null=True)
    streetAddress = models.CharField(max_length=255, blank=True, null=True)
    streetAddressCity = models.CharField(max_length=255, blank=True, null=True)
    zip = models.CharField(max_length=255, blank=True, null=True)
    amount = models.FloatField(null=True, blank=True)
    productid = models.CharField(max_length=255, blank=True, null=True)
    status =models.CharField(max_length=255, default="Pending")
    def __str__(self) -> str:
        return self.firstname + self.lastname + self.phoneNumber 

class Studentsgifts(models.Model):
    beneficiaryName = models.CharField(max_length=255)
    beneficiaryId = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    donatedBy = models.CharField(max_length=255)
    email = models.EmailField()
    paymentMode = models.CharField(max_length=100)
    paymentId = models.CharField(max_length=100)
    status =models.CharField(max_length=255, default="Pending")
    def __str__(self):
        return f"Donation for {self.beneficiaryName} - {self.amount}"

class SendPrayer(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name