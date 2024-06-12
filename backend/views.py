from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.conf import settings
from django.contrib import messages
from home.forms import *
from home.models import *
from backend.models import *
from backend.forms import *

# Authentication Section

def user_login(request):
    if request.user.is_authenticated:
        return redirect('backend:dashboard')

    form = UserLoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.email}!')
            return redirect('backend:dashboard')
        else:
            messages.error(request, 'Invalid credentials. Please check your email and password.')
            return redirect('backend:login')
    return render(request, 'backend/auth/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('backend:login')

# Dashboard Section

@login_required
def dashboard(request):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')

    getStudents = Student.objects.all().order_by('created_at')[:3]
    getBlog = Blog.objects.all().order_by('created_at')[:1]
    student_count = Student.objects.count()
    project_count = Project.objects.count()
    product_count = Product.objects.count()
    blog_count = Blog.objects.count()
    
    labels = ["January", "February", "March", "April", "May", "June", "July"]
    data = [10, 20, 15, 25, 30, 35, 40]
    
    context ={
        'getStudents': getStudents,
        'getBlog': getBlog,
        'student_count': student_count,
        'project_count': project_count,
        'product_count': product_count,
        'blog_count': blog_count,
        'labels': labels,
        'data': data,
    }

    return render(request, 'backend/dashboard.html', context)

# Student Section

@login_required
def getStudents(request):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    students = Student.objects.all()
    
    context = {
        'students': students,
    }

    return render(request, 'backend/students/index.html', context)

@login_required
def addStudent(request):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student created successfully!')
            return redirect('backend:getStudents')
        else:
            messages.error(request, 'Error creating student. Please check the form.')
    else:
        form = StudentForm()
    
    context = {
        'form': form
    }

    return render(request, 'backend/students/create.html', context)

@login_required
def editStudent(request, slug):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    student = get_object_or_404(Student, slug=slug)

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully!')
            return redirect('backend:getStudents')
        else:
            messages.error(request, 'Error updating the student. Please check the form.')
    else:
        form = StudentForm(instance=student)
        
    context = {
        'form': form,
        'student': student
    }

    return render(request, 'backend/students/edit.html', context)

@login_required
def deleteStudent(request, slug):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    if request.method == 'POST':
        student = get_object_or_404(Student, slug=slug)
        student.delete()
        messages.success(request, 'Student deleted successfully!')

    return redirect('backend:getStudents')

# Team Section

@login_required
def getTeam(request):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    team = Team.objects.all()
    
    context = {
        'team': team,
    }
    
    return render(request, 'backend/team/index.html', context)

@login_required
def addTeam(request):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Team Member created successfully!')
            return redirect('backend:getTeam')
        else:
            messages.error(request, 'Error creating a team member. Please check the form.')
    else:
        form = TeamForm()
        
    context = {
        'form': form
    }

    return render(request, 'backend/team/create.html', context)

@login_required
def editTeam(request, slug):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    person = get_object_or_404(Team, slug=slug)

    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES, instance=person)
        if form.is_valid():
            form.save()
            messages.success(request, 'Team updated successfully!')
            return redirect('backend:getTeam')
        else:
            messages.error(request, 'Error updating the team member. Please check the form.')
    else:
        form = TeamForm(instance=person)
        
    context = {
        'form': form,
        'person': person
    }

    return render(request, 'backend/team/edit.html', context)

@login_required
def deleteTeam(request, slug):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    if request.method == 'POST':
        team = get_object_or_404(Team, slug=slug)
        team.delete()
        messages.success(request, 'Team deleted successfully!')

    return redirect('backend:getTeam')

# Product Section

@login_required
def getProduct(request):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    products = Product.objects.all()
    
    context = {
        'products': products
    }
    
    return render(request, 'backend/store/index.html', context)

@login_required
def addProduct(request):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product created successfully!')
            return redirect('backend:getProduct')
        else:
            messages.error(request, 'Error creating a product. Please check the form.')
    else:
        form = ProductForm()
        
    context = {
        'form': form
    }
    
    return render(request, 'backend/store/create.html', context)

@login_required
def editProduct(request, slug):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    product = get_object_or_404(Product, slug=slug)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('backend:getProduct')
        else:
            messages.error(request, 'Error updating the product. Please check the form.')
    else:
        form = ProductForm(instance=product)
        
    context = {
        'form': form,
        'product': product
    }
    
    return render(request, 'backend/store/edit.html', context)

@login_required
def deleteProduct(request, slug):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    if request.method == 'POST':
        product = get_object_or_404(Product, slug=slug)
        product.delete()
        messages.success(request, 'Product deleted successfully!')

    return redirect('backend:getProduct')

# Projects Section

@login_required
def getProjects(request):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    projects = Project.objects.all()
    
    context = {
        'projects': projects
    }
    
    return render(request, 'backend/projects/index.html', context)

@login_required
def addProject(request):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project created successfully!')
            return redirect('backend:getProjects')
        else:
            messages.error(request, 'Error creating a project. Please check the form.')
    else:
        form = ProjectForm()
        
    context = {
        'form': form
    }

    return render(request, 'backend/projects/create.html', context)

@login_required
def editProject(request, slug):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    project = get_object_or_404(Project, slug=slug)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully!')
            return redirect('backend:getProjects')
        else:
            messages.error(request, 'Error updating the project. Please check the form.')
    else:
        form = ProjectForm(instance=project)
        
    context = {
        'form': form,
        'project': project
    }
    return render(request, 'backend/projects/edit.html', context)

@login_required
def deleteProject(request, slug):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    if request.method == 'POST':
        project = get_object_or_404(Project, slug=slug)
        project.delete()
        messages.success(request, 'Project deleted successfully!')
        
    return redirect('backend:getProjects')

# Blog Section

@login_required
def getBlog(request):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    blogs = Blog.objects.all()

    context = {
        'blogs': blogs
    }

    return render(request, 'backend/blog/index.html', context)

@login_required
def addBlog(request):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog created successfully!')
            return redirect('backend:getBlog')
        else:
            messages.error(request, 'Error creating a blog. Please check the form.')
    else:
        form = BlogForm()
        
    context = {
        'form': form
    }

    return render(request, 'backend/blog/create.html', context)

@login_required
def editBlog(request, slug):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    blog = get_object_or_404(Blog, slug=slug)

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog updated successfully!')
            return redirect('backend:getBlog')
        else:
            messages.error(request, 'Error updating the blog. Please check the form.')
    else:
        form = BlogForm(instance=blog)
        
    context = {
        'form': form,
        'blog': blog
    }

    return render(request, 'backend/blog/edit.html', context)

@login_required
def deleteBlog(request, slug):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    if request.method == 'POST':
        blog = get_object_or_404(Blog, slug=slug)
        blog.delete()
        messages.success(request, 'Blog deleted successfully!')
        
    return redirect('backend:getBlog')

@csrf_exempt
def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        path = default_storage.save(f'quill_images/{image.name}', image)
        return JsonResponse({'location': f'{settings.MEDIA_URL}{path}'})
    return JsonResponse({'error': 'Invalid request'}, status=400)

# Donate Section

@login_required
def donate(request):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    donate = Donate.objects.all()
    
    context = {
        'donate': donate
    }
    
    return render(request, 'backend/donate/donate.html', context)

@login_required
def donateToStudent(request):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    donations = StudentDonations.objects.all()
    
    context = {
        'donations': donations
    }
    
    return render(request, 'backend/donate/donate-to-student.html', context)

@login_required
def gifts(request):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    gifts = DonateGifts.objects.all()
    
    context = {
        'gifts': gifts
    }
    
    return render(request, 'backend/donate/gifts.html', context)

@login_required
def visitingRequest(request):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    requests = VisitingRequest.objects.all().order_by('-created_at')

    context = {
        'requests': requests
    }

    return render(request, 'backend/request-visit/index.html', context)

@login_required
def visitDetails(request, slug):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    visit_request = get_object_or_404(VisitingRequest, slug=slug)

    context = {
        'visit_request': visit_request
    }

    return render(request, 'backend/request-visit/show.html', context)

@login_required
def updateStatus(request, slug):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    visit_request = VisitingRequest.objects.get(slug=slug)
    visit_request.status = not visit_request.status
    visit_request.save()

    return redirect('backend:visitingRequest')

@login_required
def campaign(request):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    campaigns = Campaign.objects.all()

    context = {
        'campaigns': campaigns
    }

    return render(request, 'backend/campaign/index.html', context)

@login_required
def addCampaign(request):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    if request.method == 'POST':
        form = CampaignForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Campaign created successfully!')
            return redirect('backend:campaign')
        else:
            messages.error(request, 'Error creating campaign. Please check the form.')
    else:
        form = CampaignForm()
    
    context = {
        'form': form
    }

    return render(request, 'backend/campaign/create.html', context)


@login_required
def editCampaign(request, slug):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    campaign = get_object_or_404(Campaign, slug=slug)

    if request.method == 'POST':
        form = CampaignForm(request.POST, request.FILES, instance=campaign)
        if form.is_valid():
            form.save()
            messages.success(request, 'Campaign updated successfully!')
            return redirect('backend:campaign')
        else:
            messages.error(request, 'Error updating the campaign. Please check the form.')
    else:
        form = CampaignForm(instance=campaign)
        
    context = {
        'form': form,
        'campaign': campaign
    }

    return render(request, 'backend/campaign/edit.html', context)

@login_required
def deleteCampaign(request, slug):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    if request.method == 'POST':
        campaign = get_object_or_404(Campaign, slug=slug)
        campaign.delete()
        messages.success(request, 'Campaign deleted successfully!')

    return redirect('backend:campaign')

@login_required
def fundraising(request):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    fundraising = Fundraising.objects.all()

    context = {
        'fundraising': fundraising
    }

    return render(request, 'backend/campaign/fundraising.html', context)

@login_required
def volunteers(request):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    volunteers = Volunteer.objects.all().order_by('-created_at')

    context = {
        'volunteers': volunteers
    }

    return render(request, 'backend/volunteers/index.html', context)

@login_required
def volunteerDetails(request, slug):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    volunteer = get_object_or_404(Volunteer, slug=slug)

    context = {
        'volunteer': volunteer
    }

    return render(request, 'backend/volunteers/show.html', context)

@login_required
def volunteersUpdateStatus(request, slug):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    volunteer = Volunteer.objects.get(slug=slug)
    volunteer.status = not volunteer.status
    volunteer.save()

    return redirect('backend:volunteers')

@login_required
def resources(request):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    resources = Resource.objects.all().order_by('-created_at')

    context = {
        'resources': resources
    }

    return render(request, 'backend/resources/index.html', context)

@login_required
def addResource(request):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Resource created successfully!')
            return redirect('backend:resources')
        else:
            messages.error(request, 'Error creating a resource. Please check the form.')
    else:
        form = ResourceForm()
        
    context = {
        'form': form
    }

    return render(request, 'backend/resources/create.html', context)

@login_required
def editResource(request, slug):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    resource = get_object_or_404(Resource, slug=slug)

    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES, instance=resource)
        if form.is_valid():
            form.save()
            messages.success(request, 'Resource updated successfully!')
            return redirect('backend:resources')
        else:
            messages.error(request, 'Error updating the resource. Please check the form.')
    else:
        form = ResourceForm(instance=resource)
        
    context = {
        'form': form,
        'resource': resource
    }
    
    return render(request, 'backend/resources/edit.html', context)

@login_required
def deleteResource(request, slug):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    if request.method == 'POST':
        resource = get_object_or_404(Resource, slug=slug)
        resource.delete()
        messages.success(request, 'Resource deleted successfully!')
        
    return redirect('backend:resources')

@login_required
def setting(request):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    if request.method == 'POST':
        if 'slide_form' in request.POST:
            form = SlideForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'New slide added successfully.')
            else:
                messages.error(request, 'Error adding slide.')
        elif 'mission_vision_values_form' in request.POST:
            item_id = request.POST.get('item_id')
            item = get_object_or_404(MissionVisionValues, id=item_id)
            form = MissionVisionValuesForm(request.POST, request.FILES, instance=item)
            if form.is_valid():
                form.save()
                messages.success(request, 'Mission, vision, or value updated successfully.')
            else:
                messages.error(request, 'Error updating mission, vision, or value.')
        elif 'logo_form' in request.POST:
            form = LogoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Logo added successfully.')
            else:
                messages.error(request, 'Error adding logo.')
        elif 'edit_logo_form' in request.POST:
            logo_id = request.POST.get('logo_id')
            logo = get_object_or_404(Logo, id=logo_id)
            form = EditLogoForm(request.POST, request.FILES, instance=logo)
            if form.is_valid():
                form.save()
                messages.success(request, 'Logo updated successfully.')
            else:
                messages.error(request, 'Error updating logo.')
        elif 'delete_logo_form' in request.POST:
            logo_id = request.POST.get('logo_id')
            logo = get_object_or_404(Logo, id=logo_id)
            logo.delete()
            messages.success(request, 'Logo deleted successfully.')
        return redirect('backend:settings')
    else:
        slide_form = SlideForm()
        mission_vision_values_forms = {item.id: MissionVisionValuesForm(instance=item) for item in MissionVisionValues.objects.all()}
        logo_form = LogoForm()
        edit_logo_form = EditLogoForm()
        slides = Slide.objects.all()
        mission_vision_values = MissionVisionValues.objects.all()
        logos = Logo.objects.all()

        context = {
            'slide_form': slide_form,
            'mission_vision_values_forms': mission_vision_values_forms,
            'logo_form': logo_form,
            'edit_logo_form': edit_logo_form,
            'slides': slides,
            'mission_vision_values': mission_vision_values,
            'logos': logos,
        }

    return render(request, 'backend/settings/index.html', context)

@login_required
def edit_slide(request, slide_id):
    slide = get_object_or_404(Slide, id=slide_id)
    if request.method == 'POST':
        form = SlideForm(request.POST, request.FILES, instance=slide)
        if form.is_valid():
            form.save()
            messages.success(request, 'Slide updated successfully.')
            return redirect('backend:settings')
        else:
            messages.error(request, 'Error updating slide.')
    else:
        form = SlideForm(instance=slide)
    
    context = {
        'form': form,
        'slide': slide
    }
    return render(request, 'backend/settings/index.html', context)

@login_required
def delete_slide(request, slide_id):
    slide = get_object_or_404(Slide, id=slide_id)
    if request.method == 'POST':
        slide.delete()
        messages.success(request, 'Slide deleted successfully.')
        return redirect('backend:settings')

    context = {
        'slide': slide
    }

    return render(request, 'backend/settings/index.html', context)

@login_required
def edit_mission_vision_values(request, item_id):
    item = get_object_or_404(MissionVisionValues, id=item_id)
    if request.method == 'POST':
        form = MissionVisionValuesForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mission, Vision, or Value updated successfully.')
            return redirect('backend:settings')
        else:
            messages.error(request, 'Error updating Mission, Vision, or Value.')
    else:
        form = MissionVisionValuesForm(instance=item)
    context = {
        'form': form,
        'item': item,
    }
    return render(request, 'backend/settings/edit_mission_vision_values.html', context)

@login_required
def delete_mission_vision_values(request, item_id):
    item = get_object_or_404(MissionVisionValues, id=item_id)
    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Mission, Vision, or Value deleted successfully.')
        return redirect('backend:settings')
    context = {
        'item': item,
    }
    return render(request, 'backend/settings/delete_mission_vision_values.html', context)

@login_required
def policies(request):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    policies = Policy.objects.all()
    
    context = {
        'policies': policies,
    }
    
    return render(request, 'backend/policy/index.html', context)

@login_required
def addPolicy(request):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    if request.method == 'POST':
        form = PolicyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Policy created successfully!')
            return redirect('backend:policies')
        else:
            messages.error(request, 'Error creating a policy. Please check the form.')
    else:
        form = PolicyForm()
        
    context = {
        'form': form
    }

    return render(request, 'backend/policy/create.html', context)

@login_required
def editPolicy(request, slug):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    policy = get_object_or_404(Policy, slug=slug)

    if request.method == 'POST':
        form = PolicyForm(request.POST, request.FILES, instance=policy)
        if form.is_valid():
            form.save()
            messages.success(request, 'Policy updated successfully!')
            return redirect('backend:policies')
        else:
            messages.error(request, 'Error updating the policy. Please check the form.')
    else:
        form = PolicyForm(instance=policy)
        
    context = {
        'form': form,
        'policy': policy
    }

    return render(request, 'backend/policy/edit.html', context)

@login_required
def deletePolicy(request, slug):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('sponsor:dashboard')
    if request.method == 'POST':
        policy = get_object_or_404(Policy, slug=slug)
        policy.delete()
        messages.success(request, 'Policy deleted successfully!')

    return redirect('backend:policies')