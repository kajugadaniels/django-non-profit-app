from django.db import models
from django.utils.text import slugify
from datetime import date
from django_quill.fields import QuillField
from django.utils import timezone
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
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
    image = ProcessedImageField(
        upload_to='students/',
        processors=[ResizeToFill(1296, 1556)],
        format='JPEG',
        options={'quality': 90},
    )
    birthday = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    spo_cover = models.CharField(max_length=30, choices=SPONSORSHIP_COVER_CHOICES)
    description = models.TextField(blank=True)
    # description = QuillField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

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
    image = ProcessedImageField(
        upload_to='store/',
        processors=[ResizeToFill(800, 800)],
        format='JPEG',
        options={'quality': 90},
    )
    unit = models.CharField(max_length=255, default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    # description = QuillField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    position = models.CharField(max_length=255)
    image = models.ImageField(upload_to='team/')
    image = ProcessedImageField(
        upload_to='team/',
        processors=[ResizeToFill(1200, 1500)],
        format='JPEG',
        options={'quality': 90},
    )
    description = models.TextField()
    # description = QuillField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Team, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=255)
    subTitle = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    image = ProcessedImageField(
        upload_to='blog/',
        processors=[ResizeToFill(3600, 2026)],
        format='JPEG',
        options={'quality': 90},
    )
    description = models.TextField()
    # description = QuillField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    image = ProcessedImageField(
        upload_to='projects/',
        processors=[ResizeToFill(3600, 2026)],
        format='JPEG',
        options={'quality': 90},
    )
    description = models.TextField()
    # description = QuillField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Slide(models.Model):
    image = ProcessedImageField(
        upload_to='slides/',
        processors=[ResizeToFill(1080, 719)],
        format='JPEG',
        options={'quality': 90},
    )
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Slide {self.id}"

class Testimony(models.Model):
    name = models.CharField(max_length=100)
    image = ProcessedImageField(
        upload_to='testimonies/',
        processors=[ResizeToFill(719, 719)],
        format='JPEG',
        options={'quality': 90},
    )
    message = models.TextField(blank=True, null=True)
    position = models.CharField(max_length=100)
    youtube_link = models.URLField(blank=True, null=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name