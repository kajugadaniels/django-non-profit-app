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
    benefits = models.TextField(blank=True)
    description = models.TextField(blank=True)
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

class MissionVisionValues(models.Model):
    SECTION_CHOICES = [
        ('mission', 'Mission'),
        ('vision', 'Vision'),
        ('values', 'Values')
    ]

    section = models.CharField(max_length=10, choices=SECTION_CHOICES)
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to='icons/')

    def __str__(self):
        return f"{self.get_section_display()}: {self.title}"

class News(models.Model):
    CATEGORY_CHOICES = [
        ('vocational-training', 'Vocational Training'),
        ('education', 'Education'),
        ('tunga-mothers', 'Tunga Mothers'),
        ('community-empowerment', 'Community Empowerment'),
        ('medical-care', 'Medical Care'),
    ]
    
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    image = ProcessedImageField(
        upload_to='news/',
        processors=[ResizeToFill(3600, 2026)],
        format='JPEG',
        options={'quality': 90},
    )
    description = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(News, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Logo(models.Model):
    SECTION_CHOICES = [
        ('color_logo', 'Colored Logo'),
        ('black_logo', 'Black Logo'),
        ('white_logo', 'White Logo'),
        ('favicon', 'Favicon'),
    ]

    section = models.CharField(max_length=20, choices=SECTION_CHOICES, default='favicon', unique=True)
    image = models.ImageField(
        upload_to='logos/',
    )

    def __str__(self):
        return self.section

class VisitingRequest(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    org_name = models.CharField(max_length=255)
    n_visitors = models.PositiveIntegerField()
    req_visit = models.DateField()
    purpose = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(VisitingRequest, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    about = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Resource(models.Model):
    CATEGORY_CHOICES = [
        ('guidelines', 'Guidelines'),
        ('brochures', 'Brochures'),
        ('social_media', 'Social Media'),
        ('photos', 'Photos')
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    image = models.ImageField(upload_to='resources/', blank=True, null=True)
    file = models.FileField(upload_to='resources/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Resource, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Campaign(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='campaigns/')
    image = ProcessedImageField(
        upload_to='campaigns/',
        processors=[ResizeToFill(600, 413)],
        format='JPEG',
        options={'quality': 90},
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Campaign, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Fundraising(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='fundraising')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name