import os
from django.db import models
from django.utils.text import slugify
from datetime import date
from django_quill.fields import QuillField
from django.utils import timezone
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

def student_image_path(instance, filename):
    base_filename, file_extension = os.path.splitext(filename)
    return f'students/student_{slugify(instance.name)}_{instance.birthday}_{instance.gender}{file_extension}'

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
        upload_to=student_image_path,
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
        self.slug = slugify(self.name)
        super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

def product_image_path(instance, filename):
    base_filename, file_extension = os.path.splitext(filename)
    return f'products/product_{slugify(instance.name)}_{instance.price}{file_extension}'

class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    image = ProcessedImageField(
        upload_to=product_image_path,
        processors=[ResizeToFill(800, 800)],
        format='JPEG',
        options={'quality': 90},
    )
    unit = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

def team_image_path(instance, filename):
    base_filename, file_extension = os.path.splitext(filename)
    return f'teams/team_{slugify(instance.name)}_{instance.position}_{instance.category}{file_extension}'

class Team(models.Model):
    CATEGORY_CHOICES = [
        ('Rwanda Staff', 'Rwanda Staff'),
        ('Stateside Staff', 'Stateside Staff'),
    ]

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    position = models.CharField(max_length=255)
    image = ProcessedImageField(
        upload_to=team_image_path,
        processors=[ResizeToFill(1200, 1500)],
        format='JPEG',
        options={'quality': 90},
    )
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Team, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

def blog_image_path(instance, filename):
    base_filename, file_extension = os.path.splitext(filename)
    return f'blogs/blog_{slugify(instance.title)}_{instance.created_at}{file_extension}'

class Blog(models.Model):
    title = models.CharField(max_length=255)
    subTitle = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    image = ProcessedImageField(
        upload_to=blog_image_path,
        processors=[ResizeToFill(3600, 2026)],
        format='JPEG',
        options={'quality': 90},
    )
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

def slide_image_path(instance, filename):
    base_filename, file_extension = os.path.splitext(filename)
    return f'slides/slide_{slugify(instance.created_at)}{file_extension}'

class Slide(models.Model):
    image = ProcessedImageField(
        upload_to=slide_image_path,
        processors=[ResizeToFill(1080, 719)],
        format='JPEG',
        options={'quality': 90},
    )
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Slide {self.id}"

def testimony_image_path(instance, filename):
    base_filename, file_extension = os.path.splitext(filename)
    return f'testimonies/testimony_{slugify(instance.name)}_{instance.position}{file_extension}'

class Testimony(models.Model):
    name = models.CharField(max_length=100)
    image = ProcessedImageField(
        upload_to=testimony_image_path,
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

def story_image_path(instance, filename):
    base_filename, file_extension = os.path.splitext(filename)
    return f'stories/story_{slugify(instance.title)}_{instance.category}_{instance.created_at}{file_extension}'

class News(models.Model):
    CATEGORY_CHOICES = [
        ('Vocational Training', 'Vocational Training'),
        ('Education', 'Education'),
        ('Tunga Women Initiative', 'Tunga Women Initiative'),
        ('Community Empowerment', 'Community Empowerment'),
        ('Medical Care', 'Medical Care'),
    ]

    
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    image = ProcessedImageField(
        upload_to=story_image_path,
        processors=[ResizeToFill(3600, 2026)],
        format='JPEG',
        options={'quality': 90},
    )
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
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

def resource_image_path(instance, filename):
    base_filename, file_extension = os.path.splitext(filename)
    return f'resources/resource_{slugify(instance.title)}_{instance.category}_{instance.created_at}{file_extension}'

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
    image = models.ImageField(upload_to=resource_image_path, blank=True, null=True)
    file = models.FileField(upload_to=resource_image_path, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Resource, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

def campaign_image_path(instance, filename):
    base_filename, file_extension = os.path.splitext(filename)
    return f'campaigns/campaign_{slugify(instance.title)}_{instance.created_at}{file_extension}'

class Campaign(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    image = ProcessedImageField(
        upload_to=campaign_image_path,
        processors=[ResizeToFill(600, 413)],
        format='JPEG',
        options={'quality': 90},
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
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

class Policy(models.Model):
    CATEGORY_CHOICES = [
        ('Privacy Policy', 'Privacy Policy'),
        ('Child Protection Policy', 'Child Protection Policy'),
        ('Terms & Conditions', 'Terms & Conditions'),
    ]

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category)
        super(Policy, self).save(*args, **kwargs)

    def __str__(self):
        return self.category

def project_image_path(instance, filename):
    base_filename, file_extension = os.path.splitext(filename)
    return f'projects/project_{slugify(instance.title)}_{instance.category}_{instance.created_at}{file_extension}'

class ProjectDetails(models.Model):
    CATEGORY_CHOICES = [
        ('Special Projects', 'Special Projects'),
        ('Regular Projects', 'Regular Projects'),
        ('Normal Projects', 'Normal Projects'),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    image = ProcessedImageField(
        upload_to=project_image_path,
        processors=[ResizeToFill(3600, 2026)],
        format='JPEG',
        options={'quality': 90},
    )
    target = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(ProjectDetails, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

def reference_sheet_image_path(instance, filename):
    base_filename, file_extension = os.path.splitext(filename)
    return f'reference-sheet/reference_sheet_{slugify(instance.title)}_{instance.created_at}{file_extension}'

class ReferenceSheet(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    file = models.FileField(upload_to=reference_sheet_image_path, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(ReferenceSheet, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class JobVacancy(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    location = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    currency = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(JobVacancy, self).save(*args, **kwargs)

    def __str__(self):
        return self.title