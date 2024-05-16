from django.db import models
from django.utils.text import slugify
from datetime import date
from django_quill.fields import QuillField

class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    SPONSORSHIP_COVER_CHOICES = (
        ('School Fees', 'School Fees'),
        ('Clothes', 'Clothes'),
        ('Medicines', 'Medicines'),
        ('Food', 'Food'),
    )

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='students/', blank=True)
    birthday = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    spo_cover = models.CharField(max_length=30, choices=SPONSORSHIP_COVER_CHOICES)
    description = models.TextField()
    # description = QuillField()

    @property
    def age(self):
        today = date.today()
        age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
        return age

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='store/')
    unit = models.CharField(max_length=255, default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name